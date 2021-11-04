import click
from pegasus.cli.valuation import valuation
from pegasus.cli.grants import grants
from pegasus.cli.db import db


@click.group()
def pegasus():
    """
    Pegasus CLI
    """
    pass


pegasus.add_command(valuation)
pegasus.add_command(grants)
pegasus.add_command(db)

if __name__ == "__main__":
    pegasus()
