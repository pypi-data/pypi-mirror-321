from typing import List

from units.abstract import AbstractUnit
from units.composed_unit import ComposedUnit
from units.named_composed_unit import NamedComposedUnit

def unit(specifier: str) -> AbstractUnit: ...
def named_unit(
    symbol: str,
    numer: List[AbstractUnit],
    denom: List[AbstractUnit],
    multiplier: float = 1,
    is_si: bool = True,
) -> NamedComposedUnit: ...
def scaled_unit(
    new_symbol: str, base_symbol: str, multiplier: float, is_si: bool = False
) -> NamedComposedUnit: ...
def si_prefixed_unit(unit_str: str) -> ComposedUnit: ...
