import os
import click
from .initializer import make_structure, create_structure

@click.group()
def cli() -> None:
    """Main command group for project management."""
    pass

@cli.command()
@click.option('-n', '--name', default='puff', help='Project name (default is "puff").')
def init(name: str) -> None:
    """Initialize a project.

    This command creates the project structure with the specified name. 
    If no name is provided, the default value 'puff' is used.

    Arguments:
        name (str): The name of the project to be used for creating the structure.
    """
    base_path = os.getcwd()  # Current working directory
    create_structure(base_path, make_structure(name=name))

def main() -> None:
    """Run the CLI application."""
    if __name__ == "__main__":
        cli()
