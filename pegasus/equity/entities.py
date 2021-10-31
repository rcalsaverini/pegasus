from dataclasses import dataclass
import dataclasses
from enum import Enum
from pandas import Series


@dataclass
class Grant:
    name: str
    schedule: Series

    def net_value(self, price):
        return price


@dataclass
class OptionGrant(Grant):
    strike: float

    def net_value(self, price):
        return price - self.strike


@dataclass
class RSUGrant(Grant):
    pass
