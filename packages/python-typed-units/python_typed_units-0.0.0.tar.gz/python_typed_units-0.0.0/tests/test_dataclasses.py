from dataclasses import dataclass
from typing import Optional

from typed_units import (
    Area,
    Force,
    amp,
    amphour,
    centimeter,
    kgf,
    kilogram,
    kilometer,
    kmh,
    meter,
    ms,
    newton,
    seconds,
)


@dataclass
class SIUnitTest:
    force: Optional[Force] = None
    area: Optional[Area] = None


def test_kg_force() -> None:
    test = SIUnitTest(force=newton(3))
    assert test.force == kgf(0.3058103975535168)


def test_length() -> None:
    f = meter(5)
    g = centimeter(500)
    assert f == g
    assert f == meter(g)
    assert f == kilometer(0.005)


def test_speed() -> None:
    a = ms(50)
    b = kmh(180)
    assert a == b


def test_amp_hours() -> None:
    a = amp(5) * seconds(3600)
    b = amphour(5)
    assert a == b


def test_force() -> None:
    m = meter(5)
    kg = kilogram(14)
    s = seconds(51)
    a = m * kg / s**2

    assert newton(a)
