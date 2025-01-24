import click

from .build import build
from .clean import clean
from .create import create
from .generate import generate
from .publish import publish
from .test import test
from .update import update


@click.group(name="service")
def service_group():
    """Command family for service-related tasks."""


service_group.add_command(build)
service_group.add_command(test)
service_group.add_command(clean)
service_group.add_command(create)
service_group.add_command(generate)
service_group.add_command(update)
service_group.add_command(publish)
