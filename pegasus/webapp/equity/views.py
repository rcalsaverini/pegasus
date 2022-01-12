from flask import Blueprint, render_template, redirect, url_for

from pegasus.webapp.equity.forms import RSUForm, OptionForm
from pegasus.webapp.equity.controllers import list_grants, insert_grant, get_grant
from pegasus.equity.vesting import get_vesting_schedule, plot_grant_schedule


grants = Blueprint("grants", __name__, template_folder="templates")


@grants.route("/grants", methods=["GET", "POST"])
def all_grants():
    option_form = OptionForm()
    rsu_form = RSUForm()
    grants = list_grants()
    if option_form.submit_option.data and option_form.validate_on_submit():
        insert_grant(option_form.to_grant())
        redirect(url_for("grants.all_grants"))
    elif rsu_form.submit_rsu.data and rsu_form.validate_on_submit():
        insert_grant(rsu_form.to_grant())
        redirect(url_for("grants.all_grants"))

    return render_template(
        "grants.jinja",
        grants=grants,
        option_form=option_form,
        rsu_form=rsu_form,
    )


@grants.route("/grants/<name>")
def grant(name):
    grant = get_grant(name)
    schedule = get_vesting_schedule(grant)
    my_plot = plot_grant_schedule(schedule)
    return render_template("grant.jinja", grant=grant, plot=my_plot, schedule=schedule)
