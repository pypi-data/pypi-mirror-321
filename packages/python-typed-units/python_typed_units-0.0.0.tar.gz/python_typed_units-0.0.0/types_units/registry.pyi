"""Global registry mapping unit specifiers to unit objects."""

from typing import Dict

from units.abstract import AbstractUnit

REGISTRY: Dict[str, AbstractUnit] = {}
