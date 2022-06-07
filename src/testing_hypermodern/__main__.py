"""Command-line interface."""
import click

from . import api

@click.command()
@click.version_option()
def main() -> None:
    """Testing_Hypermodern."""
    api.something(3)
    api.something('hello')


if __name__ == "__main__":
    main(prog_name="testing_hypermodern")  # pragma: no cover
