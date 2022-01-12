from dataclasses import dataclass, fields, asdict
from pandas import to_datetime
from datetime import date


@dataclass
class Grant:
    name: str
    shares: int
    date: date
    cliff: int
    vesting: int

    def to_dict(self):
        dictionary = asdict(self)
        dictionary["date"] = dictionary["date"].strftime("%Y-%m-%d")
        return dictionary

    @classmethod
    def from_dict(cls, dictionary):
        dictionary["date"] = to_datetime((dictionary["date"]))
        return cls(**{f.name: dictionary[f.name] for f in fields(cls)})


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
