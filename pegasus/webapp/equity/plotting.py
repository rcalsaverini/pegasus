import matplotlib as mpl

mpl.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from io import BytesIO
import base64


def encode_plot(fig):
    figfile = BytesIO()
    fig.savefig(figfile, format="png")
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.read())
    return figdata_png.decode("utf-8")


def line_format(label, skip):
    """
    Convert time label to the format of pandas line plot
    """
    month = label.month_name()[:3]
    if label.month == 1 or (label.month % skip) == 0:
        month += f"\n{label.year}"
    else:
        month = ""
    return month


def dated_bar_plot(data_series, ax, fig, max_ticks, *args, **kwargs):
    data_series.plot.line(ax=ax, style="-*", *args, **kwargs)
    # ticklabels = [""] * len(data_series.index)
    # skip = len(ticklabels) // max_ticks if len(ticklabels) > max_ticks else 1
    # ticklabels = [line_format(date, skip) for date in data_series.index]
    # ax.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
    # fig.autofmt_xdate()
