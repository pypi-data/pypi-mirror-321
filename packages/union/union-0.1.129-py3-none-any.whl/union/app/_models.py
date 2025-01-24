import glob
import os
import platform
import re
import shlex
from dataclasses import dataclass, field
from datetime import timedelta
from enum import Enum
from typing import Dict, List, Optional, Union

from flyteidl.core.literals_pb2 import KeyValuePair
from flyteidl.core.tasks_pb2 import Container, ContainerPort
from flyteidl.core.tasks_pb2 import Resources as ResourcesIDL
from flytekit import FlyteContextManager, ImageSpec, Resources
from flytekit.core.artifact import ArtifactQuery
from mashumaro.codecs.json import JSONEncoder

from union.app._common import patch_get_flytekit_for_pypi, patch_get_unionai_for_pypi
from union.internal.app.app_definition_pb2 import App as AppIDL
from union.internal.app.app_definition_pb2 import (
    AutoscalingConfig,
    Identifier,
    IngressConfig,
    Meta,
    Replicas,
    Spec,
)
from union.internal.app.app_definition_pb2 import Concurrency as ConcurrencyIDL
from union.internal.app.app_definition_pb2 import RequestRate as RequestRateIDL
from union.internal.app.app_definition_pb2 import ScalingMetric as ScalingMetricIDL


@dataclass
class AppRegistry:
    """Keeps track of all user defined applications"""

    apps: Dict[str, "App"] = field(default_factory=dict)

    def add_app(self, app: "App"):
        execution_state = FlyteContextManager.current_context().execution_state
        if execution_state.mode is None and app.name in self.apps:
            # This is running in a non execute context, so we check if the app name is already used:
            msg = f"App with name: {app.name} was already defined, please use a different name"
            raise ValueError(msg)

        self.apps[app.name] = app


APP_REGISTRY = AppRegistry()
# TODO: Add more protocols here when we deploy to another cloud providers
SUPPORTED_FS_PROTOCOLS = ["s3://", "s3a://", "gs://"]


@dataclass
class URLQuery:
    name: str
    public: bool


ENV_NAME_RE = re.compile("^[_a-zA-Z][_a-zA-Z0-9]*$")
APP_NAME_RE = re.compile(r"[a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*")


def _has_file_extension(file_path) -> bool:
    _, ext = os.path.splitext(file_path)
    return bool(ext)


@dataclass
class Input:
    """
    Input for application.

    :param name: Name of input.
    :param value: Value for input.
    :param env_name: Environment name to set the value in the serving environment.
    :param download: When True, the input will be automatically downloaded. This
        only works if the value refers to an item in a object store. i.e. `s3://...`
    """

    class Type(Enum):
        File = "file"
        Directory = "directory"
        String = "string"
        _UrlQuery = "url_query"  # Private type, users should not need this

    name: str
    value: Union[str, ArtifactQuery, URLQuery]
    env_name: Optional[str] = None
    type: Optional[Type] = None
    download: bool = False
    mount: Optional[str] = None

    def __post_init__(self):
        if self.env_name is not None and ENV_NAME_RE.match(self.env_name) is None:
            msg = f"env_name ({self.env_name}) is not a valid environment name for shells"
            raise ValueError(msg)


@dataclass
class MaterializedInput:
    value: str
    type: Optional[Input.Type] = None


@dataclass
class AppSerializationSettings:
    """Runtime settings for creating an AppIDL"""

    org: str
    project: str
    domain: str

    desired_state: Spec.DesiredState
    materialized_inputs: dict[str, MaterializedInput] = field(default_factory=dict)
    additional_distribution: Optional[str] = None


@dataclass
class InputBackend:
    """
    Input information for the backend.
    """

    name: str
    value: str
    download: bool
    type: Optional[Input.Type] = None
    env_name: Optional[str] = None
    dest: Optional[str] = None

    def __post_init__(self):
        if self.type is None:
            if any(self.value.startswith(proto) for proto in SUPPORTED_FS_PROTOCOLS):
                if _has_file_extension(self.value):
                    self.type = Input.Type.File
                else:
                    self.type = Input.Type.Directory
            else:
                self.type = Input.Type.String

        if self.type == Input.Type.String:
            # Nothing to download for a string
            self.download = False

        # If the type is a file or directory and there is a destination, then we
        # automatically assume it is going to be downloaded
        # TODO: In the future, we may mount this, so there is no need to download it
        # with the runtime.
        if self.type in (Input.Type.File, Input.Type.Directory) and self.dest is not None:
            self.download = True

    @classmethod
    def from_input(cls, user_input: Input, settings: AppSerializationSettings) -> "InputBackend":
        if isinstance(user_input.value, str):
            value = user_input.value
            input_type = user_input.type
        else:
            # ArtifactQuery or URLQuery
            try:
                materialized_input = settings.materialized_inputs[user_input.name]
                value = materialized_input.value
                input_type = materialized_input.type or user_input.type
            except KeyError:
                msg = f"Did not materialize {user_input.name}"
                raise ValueError(msg)

        return InputBackend(
            name=user_input.name,
            value=value,
            download=user_input.download,
            env_name=user_input.env_name,
            type=input_type,
            dest=user_input.mount,
        )


@dataclass
class ServeConfig:
    """
    Configuration for serve runtime.

    :param code_uri: Location of user code in an object store (s3://...)
    :param user_inputs: User inputs. Passed in by `app.inputs`
    """

    code_uri: str  # location of user code
    inputs: List[InputBackend]


SERVE_CONFIG_ENCODER = JSONEncoder(ServeConfig)


@dataclass
class ResolvedInclude:
    src: str
    dest: str


class ScalingMetric:
    @dataclass(frozen=True)
    class Concurrency:
        """
        Use this to specify the concurrency metric for autoscaling, i.e. the number of concurrent requests at a replica
         at which to scale up.
        """

        val: int

        def __post_init__(self):
            if self.val < 1:
                raise ValueError("Concurrency must be greater than or equal to 1")

        def _to_union_idl(self) -> ConcurrencyIDL:
            return ConcurrencyIDL(target_value=self.val)

    @dataclass
    class RequestRate:
        """
        Use this to specify the request rate metric for autoscaling, i.e. the number of requests per second at a replica
         at which to scale up.
        """

        val: int

        def __post_init__(self):
            if self.val < 1:
                raise ValueError("Request rate must be greater than or equal to 1")

        def _to_union_idl(self) -> RequestRateIDL:
            return RequestRateIDL(target_value=self.val)

    @staticmethod
    def _to_union_idl(metric: Optional[Union[RequestRate, Concurrency]]) -> Optional[ScalingMetricIDL]:
        if metric is None:
            return None
        request_rate = None
        concurrency = None
        if isinstance(metric, ScalingMetric.RequestRate):
            request_rate = metric._to_union_idl()
        if isinstance(metric, ScalingMetric.Concurrency):
            concurrency = metric._to_union_idl()
        return ScalingMetricIDL(
            request_rate=request_rate,
            concurrency=concurrency,
        )

    @staticmethod
    def _validate(metric: Optional[Union[RequestRate, Concurrency]]):
        if metric is None:
            return
        if not isinstance(metric, (ScalingMetric.RequestRate, ScalingMetric.Concurrency)):
            raise ValueError("scaling_metric must be an instance of Concurrency or RequestRate")


@dataclass
class App:
    """
    App specification.

    :param name: The name of the application.
    :param container_image: The container image to use for the application.
    :param command: Command to start application.
    :param port: Port application listens to. Currently, this must be 8080 and the application
        must listen on 8080.
    :param requests: Compute resource requests for application.
    :param limits: Compute resource limits for application.
    :param include: Files to include for your application.
    :param inputs: Inputs for the application.
    :param env: Environment variables to set for the application.
    :param min_replicas: Minimum number of replicas (ignore if autoscaling is set).
    :param max_replicas: Maximum number of replicas (ignore if autoscaling is set).
    :param scaledown_after: Time to wait before scaling down a replica after it has been idle.
    :param scaling_metric: Autoscale based on a parameter, e.g. request rate or concurrency
      (others may be added in the future).
    :param cluster_pool: The target cluster_pool where the app should be deployed.
    """

    name: str
    container_image: Union[str, ImageSpec]
    command: Union[List[str], str]
    port: int
    limits: Resources
    requests: Resources = field(default_factory=Resources)
    min_replicas: int = 0
    max_replicas: int = 1
    scaledown_after: Optional[Union[int, timedelta]] = None
    scaling_metric: Optional[Union[ScalingMetric.Concurrency, ScalingMetric.RequestRate]] = None
    include: List[str] = field(default_factory=list)
    inputs: List[Input] = field(default_factory=list)
    env: dict = field(default_factory=dict)
    cluster_pool: str = "default"

    _include_resolved: List[ResolvedInclude] = field(default_factory=list)

    def _validate_autoscaling_config(self):
        if self.min_replicas < 0:
            raise ValueError("min_replicas must be greater than or equal to 0")
        if self.max_replicas < 1 or self.max_replicas < self.min_replicas:
            raise ValueError(f"max_replicas must be greater than or equal to 1 or min_replicas:{self.min_replicas}")
        if self.scaledown_after is not None:
            if isinstance(self.scaledown_after, int):
                self.scaledown_after = timedelta(seconds=self.scaledown_after)
            if self.scaledown_after.total_seconds() < 0:
                raise ValueError("scaledown_after must be greater than or equal to 0")
        ScalingMetric._validate(self.scaling_metric)

    def __post_init__(self):
        self._validate_autoscaling_config()
        match_re = APP_NAME_RE.fullmatch(self.name)
        if not match_re:
            raise ValueError("App name must consist of lower case alphanumeric characters, '-' or '.'")

        APP_REGISTRY.add_app(self)

    def _resolve_include(self, app_directory: str, cwd: str) -> "App":
        """Resolve include based on the working_dir.

        If a path in `include` is prefixed with "./", then those files are
        assumed to be relative to the file that has the App object.
        """
        relative_prefix = "./"
        seen_dests = set()

        included_resolved = []

        for file in self.include:
            normed_file = os.path.normpath(file)
            if file.startswith(relative_prefix):
                # File is relative to the app_directory:
                src_dir = app_directory
            else:
                src_dir = cwd

            src = os.path.join(src_dir, normed_file)

            if "*" in src:
                new_srcs = glob.glob(src, recursive=True)
            else:
                new_srcs = [src]

            for new_src in new_srcs:
                dest = os.path.relpath(new_src, src_dir)
                if platform.system() == "Windows":
                    # The runtime is linux so the destinations need to be understood by linux.
                    dest = dest.replace(os.sep, "/")

                if dest in seen_dests:
                    msg = f"{dest} is in include multiple times. Please remove one of them."
                    raise ValueError(msg)

                seen_dests.add(dest)

                included_resolved.append(ResolvedInclude(src=new_src, dest=dest))

        self._include_resolved = included_resolved
        return self

    def _get_image(self) -> str:
        if isinstance(self.container_image, str):
            return self.container_image

        # Build for image Spec
        from flytekit.image_spec.image_spec import ImageBuildEngine

        # TODO: Remove this patching
        # Do not install flytekit or union when building image
        with patch_get_flytekit_for_pypi(), patch_get_unionai_for_pypi():
            ImageBuildEngine.build(self.container_image)
        return self.container_image.image_name()

    def _get_command(self, settings: AppSerializationSettings) -> List[str]:
        args = ["union-serve"]

        serve_config = ServeConfig(
            code_uri=settings.additional_distribution,
            inputs=[InputBackend.from_input(user_input, settings) for user_input in self.inputs],
        )
        args.extend(["--config", SERVE_CONFIG_ENCODER.encode(serve_config)])

        if isinstance(self.command, str):
            command = shlex.split(self.command)
        else:
            command = self.command

        return args + ["--"] + command

    def _get_resources(self) -> ResourcesIDL:
        requests = []
        limits = []

        if self.requests.cpu is not None:
            requests.append(
                ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.CPU, value=str(self.requests.cpu))
            )
        if self.requests.mem is not None:
            requests.append(
                ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.MEMORY, value=str(self.requests.mem))
            )
        if self.requests.gpu is not None:
            requests.append(
                ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.GPU, value=str(self.requests.gpu))
            )
        if self.requests.ephemeral_storage is not None:
            requests.append(
                ResourcesIDL.ResourceEntry(
                    name=ResourcesIDL.ResourceName.EPHEMERAL_STORAGE, value=str(self.requests.ephemeral_storage)
                )
            )

        if self.limits.cpu is not None:
            limits.append(ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.CPU, value=str(self.limits.cpu)))
        if self.limits.mem is not None:
            limits.append(ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.MEMORY, value=str(self.limits.mem)))
        if self.limits.gpu is not None:
            limits.append(ResourcesIDL.ResourceEntry(name=ResourcesIDL.ResourceName.GPU, value=str(self.limits.gpu)))
        if self.limits.ephemeral_storage is not None:
            limits.append(
                ResourcesIDL.ResourceEntry(
                    name=ResourcesIDL.ResourceName.EPHEMERAL_STORAGE, value=str(self.limits.ephemeral_storage)
                )
            )

        return ResourcesIDL(requests=requests, limits=limits)

    def _get_container(self, settings: AppSerializationSettings) -> Container:
        return Container(
            image=self._get_image(),
            command=[],
            args=self._get_command(settings),
            resources=self._get_resources(),
            ports=[
                ContainerPort(container_port=self.port),
            ],
            env=[KeyValuePair(key=k, value=v) for k, v in self.env.items()],
        )

    def _to_union_idl(self, settings: AppSerializationSettings) -> AppIDL:
        scaling_metric = ScalingMetric._to_union_idl(self.scaling_metric)

        dur = None
        if self.scaledown_after:
            from google.protobuf.duration_pb2 import Duration

            dur = Duration()
            dur.FromTimedelta(self.scaledown_after)

        autoscaling = AutoscalingConfig(
            replicas=Replicas(min=self.min_replicas, max=self.max_replicas),
            scaledown_period=dur,
            scaling_metric=scaling_metric,
        )
        return AppIDL(
            metadata=Meta(
                id=Identifier(
                    org=settings.org,
                    project=settings.project,
                    domain=settings.domain,
                    name=self.name,
                ),
            ),
            spec=Spec(
                container=self._get_container(settings),
                desired_state=settings.desired_state,
                ingress=IngressConfig(private=False),
                autoscaling=autoscaling,
                cluster_pool=self.cluster_pool,
            ),
        )

    def query_endpoint(self, *, public: bool) -> URLQuery:
        """
        Query for endpoint.

        :param public: Whether to return the public or internal endpoint.
        :returns: Object representing a URL query.
        """
        return URLQuery(name=self.name, public=public)


@dataclass
class Endpoint(App):
    """
    Endpoint specification.

    :param name: The name of the application.
    :param container_image: The container image to use for the application.
    :param command: Command to start application.
    :param port: Port application listens to. Currently, this must be 8080 and the application
        must listen on 8080.
    :param requests: Compute resource requests for application.
    :param limits: Compute resource limits for application.
    :param include: Files to include for your application.
    :param inputs: Inputs for the application.
    """
