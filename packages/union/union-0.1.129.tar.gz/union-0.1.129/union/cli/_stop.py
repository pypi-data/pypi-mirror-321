import rich_click as click

from union._config import _DEFAULT_DOMAIN, _DEFAULT_PROJECT_BYOC
from union.remote._app_remote import AppRemote


@click.group()
def stop():
    """Stop a resource."""


@stop.command()
@click.option("--name", type=str, required=True)
@click.option("--project", default=_DEFAULT_PROJECT_BYOC, help="Project name")
@click.option("--domain", default=_DEFAULT_DOMAIN, help="Domain name")
def apps(name: str, project: str, domain: str):
    app_remote = AppRemote(project=project, domain=domain)
    app_remote.stop(name=name)
