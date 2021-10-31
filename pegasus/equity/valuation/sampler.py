from typing import List
from pandas import DataFrame
from dataclasses import dataclass
from scipy.stats._distn_infrastructure import rv_frozen


@dataclass
class Valuation:
    value: float
    stock_price: float

    @property
    def stock_ratio(self):
        return self.stock_price / self.value


class ValuationSampler:
    def __init__(self, value_distribution: rv_frozen, reference_valuation: Valuation):
        self.value_distribution = value_distribution
        self.reference_valuation = reference_valuation

    def __call__(self, num_samples: int) -> List[Valuation]:
        valuation_samples = self.value_distribution.rvs(size=num_samples)
        stock_prices = valuation_samples * self.reference_valuation.stock_ratio
        return [
            Valuation(value=value, stock_price=stock_price)
            for value, stock_price in zip(valuation_samples, stock_prices)
        ]
