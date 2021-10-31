from pegasus.equity.valuation import get_grant_values


from pegasus.equity.valuation import get_grant_values
from pegasus.equity.entities import RSUGrant
from pandas import Series, to_datetime
from numpy import array
from numpy.testing import assert_almost_equal, assert_array_equal
from pandas.testing import assert_series_equal, assert_index_equal


def test_get_grant_values():
    schedule = Series([100, 100], index=to_datetime(["2020-10-01", "2020-11-01"]))
    grant = RSUGrant("chipotle", schedule)
    output = get_grant_values(grant, 10)
    assert_array_equal(output.values, array([1000, 1000]))
    assert_index_equal(output.index, schedule.index)
