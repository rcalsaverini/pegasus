from pegasus.equity.entities import RSUGrant, OptionGrant
from pegasus.webapp.db import query_many, query_one, insert_one


def grant_from_row(row):
    klass = OptionGrant if row["kind"] == "OPTION" else RSUGrant
    row_dict = dict(**row)
    return klass.from_dict(row_dict)


def grant_to_row(grant):
    return (
        grant.name,
        grant.kind,
        grant.shares,
        grant.date,
        grant.cliff,
        grant.vesting,
        grant.strike if grant.kind == "OPTION" else None,
    )


def list_grants():
    rows = query_many("SELECT * FROM grants")
    return [grant_from_row(row) for row in rows]


def get_grant(name):
    row = query_one("SELECT * FROM grants WHERE name = ?", (name,))
    return grant_from_row(row)


def insert_grant(grant):
    query = "INSERT INTO grants (name, kind, shares, date, cliff, vesting, strike) VALUES (?, ?, ?, ?, ?, ?, ?);"
    return insert_one(query, grant_to_row(grant))
