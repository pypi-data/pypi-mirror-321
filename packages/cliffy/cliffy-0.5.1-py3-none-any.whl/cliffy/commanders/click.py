import datetime

from cliffy.commander import Commander, Group
from cliffy.manifest import Command


class ClickCommander(Commander):
    """Generates commands based on the command config"""

    def add_base_imports(self) -> None:
        self.cli = f"""## Generated {self.manifest.name} on {datetime.datetime.now()}
import rich_click as click
import subprocess
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
"""

    def add_base_cli(self) -> None:
        self.cli += f"""
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option('{self.manifest.version}')
def cli():
    pass
"""

    def add_group_command(self, command: Command) -> None:
        self.cli += f"""
@cli.command()
def {command.name}():
    \"\"\"Help for {command.name}\"\"\"
    {self.parser.parse_command_run(command)}
"""

    def add_sub_command(self, command: Command, group: Group) -> None:
        self.cli += f"""
@{group}.command()
def {command.name}():
    \"\"\"Help for {command.name}\"\"\"
    {self.parser.parse_command_run(command)}
"""
