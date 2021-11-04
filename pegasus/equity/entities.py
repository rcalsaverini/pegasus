from dataclasses import dataclass
from enum import Enum
from pandas import Series
from datetime import date


@dataclass
class Grant:
    name: str
    shares: int
    date: date
    cliff: int
    vesting: int


@dataclass
class RSUGrant(Grant):
    kind: str = "RSU"


@dataclass
class OptionGrant(Grant):
    strike: float
    kind: str = "OPTION"


# @dataclass
# class Grant:
#     name: str
#     schedule: Series

#     def net_value(self, price):
#         return price


# @dataclass
# class OptionGrant(Grant):
#     strike: float

#     def net_value(self, price):
#         return price - self.strike


# @dataclass
# class RSUGrant(Grant):
#     pass
