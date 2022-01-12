import numpy
from pegasus.equity.entities import Grant
from pandas import date_range, DataFrame
from numpy import zeros
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt

from pegasus.webapp.equity.plotting import dated_bar_plot, encode_plot


def get_vesting_schedule(grant: Grant):
    start_date = grant.date + relativedelta(years=grant.cliff)
    end_date = start_date + relativedelta(months=12 * grant.vesting - 1)
    dates = date_range(start_date, end_date, freq="1M")
    schedule = DataFrame(
        {"vested": zeros(len(dates)), "unvested": zeros(len(dates))},
        index=dates,
        dtype=int,
    )
    unvested = grant.shares
    vested = 0
    for date in dates:
        to_vest = min(round(grant.shares / len(dates)), unvested)
        vested += to_vest
        unvested -= to_vest
        schedule.loc[date] = [vested, unvested]
    return schedule


def plot_grant_schedule(grant_schedule):
    fig, ax = plt.subplots()
    dated_bar_plot(
        grant_schedule.vested,
        ax,
        fig,
        12,
        label="Vested shares",
        fontsize=12,
        color="#2ecc71",
    )

    ax.legend(loc="upper left")
    ax.set_title("Vesting schedule", fontsize=16)
    ax.set_xlabel("Date", fontsize=14)
    ax.set_ylabel("# of shares", fontsize=14)
    fig.tight_layout()
    return encode_plot(fig)
