"""Module to manage applications on Union."""

import asyncio
import logging
import os
import tarfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List, Optional

import grpc
from click import ClickException
from flyteidl.core.tasks_pb2 import Resources
from flytekit.configuration import Config
from flytekit.core.artifact import ArtifactQuery
from flytekit.models.core.types import BlobType
from rich.console import Console

from union._async import merge
from union._config import (
    ConfigSource,
    ConfigWithSource,
    _get_config_obj,
    _get_organization,
)
from union.app import App
from union.app._models import AppSerializationSettings, Input, MaterializedInput, URLQuery
from union.cli._common import _get_channel_with_org
from union.internal.app.app_definition_pb2 import App as AppIDL
from union.internal.app.app_definition_pb2 import Identifier, Spec, Status
from union.internal.app.app_logs_payload_pb2 import TailLogsRequest, TailLogsResponse
from union.internal.app.app_logs_service_pb2_grpc import AppLogsServiceStub
from union.internal.app.app_payload_pb2 import (
    CreateRequest,
    CreateResponse,
    GetRequest,
    GetResponse,
    ListResponse,
    UpdateRequest,
    UpdateResponse,
    WatchRequest,
    WatchResponse,
)
from union.internal.app.app_payload_pb2 import (
    ListRequest as ListAppsRequest,
)
from union.internal.app.app_service_pb2_grpc import AppServiceStub
from union.internal.common.identifier_pb2 import ProjectIdentifier
from union.internal.common.list_pb2 import ListRequest
from union.remote._remote import UnionRemote

logger = logging.getLogger(__name__)

FILES_TAR_FILE_NAME = "include-files.tar.gz"


class AppRemote:
    def __init__(
        self,
        project: str,
        domain: str,
        config: Optional[Config] = None,
    ):
        if config is None:
            config = _get_config_obj(config, default_to_union_semantics=True)
        else:
            config_with_source = ConfigWithSource(config=config, source=ConfigSource.REMOTE)

            config = _get_config_obj(config_with_source, default_to_union_semantics=True)

        self.config = config
        self.project = project
        self.domain = domain
        self._union_remote = UnionRemote(config=config, default_domain=domain, default_project=project)

    def list(self) -> List[AppIDL]:
        def create_list_request(token: str):
            return ListAppsRequest(
                request=ListRequest(token=token),
                org=self.org,
                project=ProjectIdentifier(name=self.project, domain=self.domain, organization=self.org),
            )

        results = []
        response: ListResponse
        token, has_next = "", True

        while has_next:
            list_request = create_list_request(token=token)

            response = self.sync_client.List(list_request)
            token = response.token
            has_next = token != ""

            results.extend(response.apps)

        return results

    def create_or_update(self, app: App):
        try:
            self.get(name=app.name)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                self.create(app)
                return
            raise

        try:
            self.update(app)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ABORTED and "Either the change has already" in e.details():
                console = Console()
                console.print(f"{app.name} app was already deployed with the current spec")
                return
            raise

    def get(self, name: str) -> AppIDL:
        app_id = Identifier(org=self.org, project=self.project, domain=self.domain, name=name)
        get_app_request = GetRequest(app_id=app_id)

        get_response: GetResponse = self.sync_client.Get(get_app_request)
        app = get_response.app

        return app

    def start(self, name: str):
        app_idl = self.get(name)
        app_idl.spec.desired_state = Spec.DesiredState.DESIRED_STATE_STARTED

        def run_request():
            update_request = UpdateRequest(app=app_idl)
            update_response: UpdateResponse = self.sync_client.Update(update_request)
            return update_response.app

        self._watch_update(app_idl, run_request)

    def update(self, app: App):
        additional_distribution = self.upload_files(app)
        materialized_input_values = self.materialize_values(app)

        settings = AppSerializationSettings(
            org=self.org,
            project=self.project,
            domain=self.domain,
            additional_distribution=additional_distribution,
            desired_state=Spec.DesiredState.DESIRED_STATE_STARTED,
            materialized_inputs=materialized_input_values,
        )
        new_app_idl = app._to_union_idl(settings=settings)

        get_app_request = GetRequest(app_id=new_app_idl.metadata.id)
        get_response: GetResponse = self.sync_client.Get(get_app_request)

        old_app_idl = get_response.app

        updated_app_idl = AppIDL(
            metadata=old_app_idl.metadata,
            spec=new_app_idl.spec,
            status=old_app_idl.status,
        )

        def run_request():
            update_request = UpdateRequest(app=updated_app_idl)
            update_response: UpdateResponse = self.sync_client.Update(update_request)
            return update_response.app

        self._watch_update(updated_app_idl, run_request)

    def create(self, app: App):
        additional_distribution = self.upload_files(app)
        materialized_input_values = self.materialize_values(app)

        settings = AppSerializationSettings(
            org=self.org,
            project=self.project,
            domain=self.domain,
            additional_distribution=additional_distribution,
            desired_state=Spec.DesiredState.DESIRED_STATE_STARTED,
            materialized_inputs=materialized_input_values,
        )
        app_idl = app._to_union_idl(settings=settings)

        def run_request():
            create_request = CreateRequest(app=app_idl)
            create_response: CreateResponse = self.sync_client.Create(create_request)
            return create_response.app

        self._watch_update(app_idl, run_request)

    def _watch_update(self, app_idl, run_request):
        console = Console()
        name = app_idl.metadata.id.name

        _console_url = self.generate_console_url(app_idl)
        console_url = f"[link={_console_url}]{_console_url}[/link]"
        console.print(f"✨ Deploying Application: [link={_console_url}]{name}[/link]")
        console.print(f"🔎 Console URL: {console_url}")

        updated_idl = run_request()
        watch_request = WatchRequest(app_id=updated_idl.metadata.id)

        async def watch_status(console):
            response: WatchResponse
            latest_message = ""
            async for response in self.async_client.Watch(watch_request):
                status = response.update_event.updated_app.status
                if not status.conditions:
                    continue
                latest_condition = status.conditions[-1]
                deployment_status = latest_condition.deployment_status
                status_str = Status.DeploymentStatus.Name(deployment_status).split("_")[-1].title()

                if latest_condition.message != latest_message:
                    console.print(f"[bold]\\[Status][/] [italic]{status_str}:[/] {latest_condition.message}")
                    latest_message = latest_condition.message

                if deployment_status in (
                    Status.DeploymentStatus.DEPLOYMENT_STATUS_UNSPECIFIED,
                    Status.DeploymentStatus.DEPLOYMENT_STATUS_STOPPED,
                    Status.DeploymentStatus.DEPLOYMENT_STATUS_FAILED,
                ):
                    raise ClickException("Application failed to deploy")
                elif deployment_status == Status.DEPLOYMENT_STATUS_UNASSIGNED:
                    raise ClickException("Application was unassigned")
                elif deployment_status == Status.DeploymentStatus.DEPLOYMENT_STATUS_STARTED:
                    yield True

        async def watch(console):
            async for to_stop in merge(watch_status(console), self._watch_logs(updated_idl, console)):
                if to_stop:
                    return

        loop = asyncio.get_event_loop()
        loop.run_until_complete(watch(console))

        _url = updated_idl.status.ingress.public_url
        url = f"[link={_url}]{_url}[/link]"

        console.print()
        console.print(f"🚀 Deployed Endpoint: {url}")

    @staticmethod
    def _format_line(line) -> str:
        whitespace_idx = line.find(" ")
        if whitespace_idx == -1:
            return line
        datetime_str = line[:whitespace_idx]

        try:
            dt = datetime.fromisoformat(datetime_str)
        except ValueError:
            return line

        formatted_dt = dt.strftime("%H:%M:%S")
        return f"{formatted_dt}{line[whitespace_idx:]}"

    async def _watch_logs(self, app_idl: AppIDL, console: Console):
        async_log_client = AppLogsServiceStub(self.async_channel)
        tail_request = TailLogsRequest(app_id=app_idl.metadata.id)
        response: TailLogsResponse
        async for response in async_log_client.TailLogs(tail_request):
            for log in response.batches.logs:
                for line in log.lines:
                    formatted_line = self._format_line(line).strip()
                    if not formatted_line:
                        continue
                    console.print(f"[bold]\\[App][/] {formatted_line}")
                    # TODO: Detect errors and stop

            yield False

    def stop(self, name: str):
        app_idl = self.get(name)
        app_idl.spec.desired_state = Spec.DesiredState.DESIRED_STATE_STOPPED

        console = Console()

        console_url = self.generate_console_url(app_idl)
        console.print(f"🛑 Stopping Application: [link={console_url}]{name}[/link]")

        update_request = UpdateRequest(app=app_idl)
        self.sync_client.Update(update_request)

    def upload_files(self, app: App) -> Optional[str]:
        """Upload files required by app."""
        if not app.include:
            return None

        with TemporaryDirectory() as temp_dir:
            tar_path = os.path.join(temp_dir, FILES_TAR_FILE_NAME)
            with tarfile.open(tar_path, "w:gz") as tar:
                for resolve_include in app._include_resolved:
                    tar.add(resolve_include.src, arcname=resolve_include.dest)

            _, upload_native_url = self._union_remote.upload_file(Path(tar_path))

            return upload_native_url

    def materialize_values(self, app: App) -> dict:
        output = {}
        for user_input in app.inputs:
            if isinstance(user_input.value, ArtifactQuery):
                query = deepcopy(user_input.value)
                query.project = self.project
                query.domain = self.domain

                result = self._union_remote.get_artifact(query=query.to_flyte_idl())
                scalar = result.literal.scalar

                input_type = None
                if scalar.blob is not None:
                    # Handle FlyteFiles and FlyteDirectories
                    if scalar.blob.metadata.type.dimensionality == BlobType.BlobDimensionality.SINGLE:
                        input_type = Input.Type.File
                    elif scalar.blob.metadata.type.dimensionality == BlobType.BlobDimensionality.MULTIPART:
                        input_type = Input.Type.Directory
                    value = result.literal.scalar.blob.uri
                elif scalar.primitive.string_value is not None:
                    value = scalar.primitive.string_value
                    input_type = Input.Type.String
                else:
                    msg = f"{scalar} is not supported as an App input"
                    raise ValueError(msg)

                output[user_input.name] = MaterializedInput(
                    value=value,
                    type=input_type,
                )

            elif isinstance(user_input.value, URLQuery):
                query = user_input.value
                # TODO: Assuming application has the same project and domain
                # TODO: Raise more informative error the assumption does not hold
                app_idl = self.get(name=query.name)
                if user_input.value.public:
                    output[user_input.name] = MaterializedInput(
                        value=app_idl.status.ingress.public_url,
                        type=Input.Type.String,
                    )
                else:
                    app_id = app_idl.metadata.id
                    output[user_input.name] = MaterializedInput(
                        value=app_id.name,
                        type=Input.Type._UrlQuery,
                    )

        return output

    def generate_console_url(self, app_idl: AppIDL) -> str:
        """Generate console url for app_idl."""
        http_domain = self._union_remote.generate_console_http_domain()
        org = _get_organization(self.config.platform, self.sync_channel)

        app_id = app_idl.metadata.id

        if org is None or org == "":
            console = "console"
        else:
            console = f"org/{org}"

        return f"{http_domain}/{console}/projects/{app_id.project}/domains/{app_id.domain}/apps/{app_id.name}"

    @property
    def sync_channel(self) -> grpc.Channel:
        try:
            return self._sync_channel
        except AttributeError:
            self._sync_channel, self._org = _get_channel_with_org(self.config.platform)
            return self._sync_channel

    @property
    def org(self) -> Optional[str]:
        try:
            return self._org
        except AttributeError:
            self._sync_channel, self._org = _get_channel_with_org(self.config.platform)
            if self._org is None or self._org == "":
                self._org = self.config.platform.endpoint.split(".")[0]
            return self._org

    @property
    def sync_client(self) -> AppServiceStub:
        try:
            return self._sync_client
        except AttributeError:
            self._sync_client = AppServiceStub(self.sync_channel)
            return self._sync_client

    @property
    def async_client(self) -> AppServiceStub:
        try:
            return self._async_client
        except AttributeError:
            self._async_client = AppServiceStub(self.async_channel)
            return self._async_client

    @property
    def async_channel(self) -> grpc.aio.Channel:
        from union.filesystems._endpoint import _create_secure_channel_from_config

        try:
            return self._async_channel
        except AttributeError:
            self._async_channel = _create_secure_channel_from_config(self.config.platform, self.sync_channel)
            return self._async_channel

    @staticmethod
    def deployment_status(app_idl: AppIDL) -> str:
        try:
            current_status = app_idl.status.conditions[-1].deployment_status
            return Status.DeploymentStatus.Name(current_status).split("_")[-1].title()
        except Exception:
            return "Unknown"

    @staticmethod
    def desired_state(app_idl: AppIDL) -> str:
        return Spec.DesiredState.Name(app_idl.spec.desired_state).split("_")[-1].title()

    @staticmethod
    def get_limits(app_idl: AppIDL) -> dict:
        output = {}
        for limit in app_idl.spec.container.resources.limits:
            if limit.name == Resources.ResourceName.CPU:
                output["cpu"] = limit.value
            if limit.name == Resources.ResourceName.MEMORY:
                output["memory"] = limit.value
        return output
