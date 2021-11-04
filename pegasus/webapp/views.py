from flask import Blueprint, render_template
from pandas import to_datetime
from pegasus.webapp.db import query_many, query_one
from pegasus.equity.entities import RSUGrant, OptionGrant
from pegasus.equity.vesting import get_vesting_schedule

grants = Blueprint("grants", __name__, template_folder="templates")


def parse_grant(row):
    if row["kind"] == "OPTION":
        return OptionGrant(
            row["name"],
            row["shares"],
            to_datetime(row["date"]),
            row["cliff"],
            row["vesting"],
            row["strike"],
        )
    elif row["kind"] == "RSU":
        return RSUGrant(
            row["name"],
            row["shares"],
            to_datetime(row["date"]),
            row["cliff"],
            row["vesting"],
        )
    else:
        raise ValueError("Unknown grant kind: {}".format(row["kind"]))


def list_grants():
    rows = query_many("SELECT * FROM grants")
    return [parse_grant(row) for row in rows]


def get_grant(name):
    row = query_one("SELECT * FROM grants WHERE name = ?", (name,))
    return parse_grant(row)


@grants.route("/grants")
def all_grants():
    grants = list_grants()
    print(grants)
    return render_template("grants.jinja", grants=grants)


@grants.route("/grants/<name>")
def grant(name):
    grant = get_grant(name)
    return render_template(
        "grant.jinja", grant=grant, schedule=get_vesting_schedule(grant)
    )
