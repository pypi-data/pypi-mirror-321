#!/bin/python
import logging

import click

from gscli.codemod.commands import codemod
from gscli.generate.commands import generate


@click.group()
def cli() -> None:
    pass


# ============= Import all command groups =============
cli.add_command(codemod)
cli.add_command(generate)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    cli()


if __name__ == "__main__":
    main()
