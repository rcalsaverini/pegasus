import sqlite3 as sql
import click


@click.group()
def db():
    pass


@db.command()
@click.option("--path", default="database/test.db", help="Database file.")
def initialize(path):
    connection = sql.connect(database=path)
    with open("database/initialization.sql", mode="r") as f:
        connection.executescript(f.read())
