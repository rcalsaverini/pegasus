from pegasus.equity.valuation.sampler import ValuationSampler
from pegasus.equity.entities import Grant
from typing import List
from pandas import DataFrame, MultiIndex


def get_grant_values(grant: Grant, stock_price: float):
    """
    Calculates the value of a grant over its schedule.
    """
    added_gross_value = grant.schedule * stock_price
    added_net_value = grant.schedule * grant.net_value(stock_price)
    data = [
        grant.schedule,
        added_gross_value,
        added_net_value,
        added_net_value.cumsum(),
    ]
    columns = ["schedule", "added_gross_value", "net_value", "cumulative_net_value"]
    output = DataFrame(data, columns=MultiIndex.from_product([[grant.name], columns]))
    return output
