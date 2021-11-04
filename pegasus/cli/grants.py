import click
from loguru import logger

from pegasus.equity.entities import RSUGrant


@click.group()
def grants():
    pass


@grants.group()
def rsu():
    pass


@rsu.command()
@click.argument("name", type=click.STRING)
@click.argument("shares", type=click.INT)
@click.argument("date", type=click.DateTime())
@click.argument("cliff", type=click.INT)
@click.argument("vesting", type=click.INT)
def create(name, shares, cliff, date, vesting):
    """Create a new grant"""
    logger.info(f"Creating RSU grant - {name}")
    logger.info(f"shares: {shares}, cliff: {cliff}, date: {date}, vesting: {vesting}")
    grant = RSUGrant(name, shares, date.date(), cliff, vesting)
    logger.info(grant)
