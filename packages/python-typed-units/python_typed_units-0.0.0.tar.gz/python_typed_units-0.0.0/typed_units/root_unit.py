from typing import Dict, Generic, Type, TypeVar

from units.compatibility import compatible  # type: ignore
from units.exception import IncompatibleUnitsError
from units.leaf_unit import LeafUnit
from units.quantity import Quantity
from units.registry import REGISTRY  # type: ignore

T = TypeVar("T", bound="RootUnit")
S = TypeVar("S", bound=Quantity)


class RootUnit(LeafUnit, Generic[S]):
    quantity_cls: Type[S]
    specifier: property

    def __new__(cls, specifier: str, is_si: bool):
        # pylint: disable=W0613
        registry: Dict[str, RootUnit[S]] = REGISTRY
        if specifier not in registry:
            registry[specifier] = super(RootUnit, cls).__new__(cls, specifier, is_si)
        return registry[specifier]

    @classmethod
    def unit(cls: Type[T], specifier: str) -> T:
        """Main factory for units."""
        registry: Dict[str, T] = REGISTRY
        if specifier in registry:
            return registry[specifier]

        return cls(specifier, is_si=False)

    def __repr__(self):
        return (
            "RootUnit("
            + ", ".join([repr(x) for x in [self.specifier, self.is_si()]])
            + ")"
        )

    def __call__(self, quantity: Quantity | float | int) -> S:
        """Overload the function call operator to convert units."""

        if not hasattr(quantity, "unit"):
            return self.quantity_cls(quantity, self)  # type: ignore

        elif isinstance(quantity, Quantity) and compatible(self, quantity.unit):
            return self.quantity_cls(  # type: ignore
                quantity.num * quantity.unit.squeeze() / self.squeeze(), self
            )
        else:
            assert hasattr(quantity, "unit")
            unit = quantity.unit  # type: ignore
            is_quantity = isinstance(quantity, Quantity)  # type: ignore
            raise IncompatibleUnitsError(
                f"Unit {self} is not compatible with {unit}"
                f" is it instance of quantity {is_quantity}"
            )
