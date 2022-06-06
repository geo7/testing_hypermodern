"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Testing_Hypermodern."""


if __name__ == "__main__":
    main(prog_name="testing_hypermodern")  # pragma: no cover
