from units import REGISTRY  # noqa
from units import ComposedUnit, NamedComposedUnit, named_unit, scaled_unit, unit
from units.quantity import Quantity

from .root_unit import RootUnit

__all__ = [
    "Mass",
    "Acceleration",
    "Distance",
    "ElectricCurrent",
    "Substance",
    "LuminousIntensity",
    "Area",
    "Force",
    "Volume",
    "Steradian",
    "gram",
    "tonne",
    "meter",
    "kilometer",
    "centimeter",
    "millimeter",
    "Time",
    "seconds",
    "minutes",
    "hours",
    "days",
    "week",
    "amp",
    "mol",
    "candela",
    "steradian",
    "liter",
    "cubic_meter",
    "square_meter",
    "newton",
    "kgf",
    "kmh",
    "ms",
    "kg_m3",
]


""" Typed classes to reference
"""


class Mass(Quantity):
    pass


class MassUnit(RootUnit[Mass]):
    quantity_cls = Mass


class Acceleration(Quantity):
    pass


class AccelerationUnit(RootUnit[Acceleration]):
    quantity_cls = Acceleration


class Density(Quantity):
    pass


class DensityUnit(RootUnit[Density]):
    quantity_cls = Density


class Distance(Quantity):
    pass


class DistanceUnit(RootUnit[Distance]):
    quantity_cls = Distance


class Time(Quantity):
    pass


class TimeUnit(RootUnit[Time]):
    quantity_cls = Time


class ElectricCurrent(Quantity):
    pass


class ElectricCurrentUnit(RootUnit[ElectricCurrent]):
    quantity_cls = ElectricCurrent


class Temperature(Quantity):
    pass


class TemperatureUnit(RootUnit[Temperature]):
    quantity_cls = Temperature


class Substance(Quantity):
    pass


class SubstanceUnit(RootUnit[Substance]):
    quantity_cls = Substance


class LuminousIntensity(Quantity):
    pass


class LuminousIntensityUnit(RootUnit[LuminousIntensity]):
    quantity_cls = LuminousIntensity


class CurrentOverTime(Quantity):
    pass


class CurrentOverTimeUnit(RootUnit[CurrentOverTime]):
    quantity_cls = CurrentOverTime


class Voltage(Quantity):
    pass


class VoltageUnit(RootUnit[Voltage]):
    quantity_cls = Voltage


class Steradian(Quantity):
    pass


class SteradianUnit(RootUnit[Steradian]):
    quantity_cls = Steradian


class Speed(Quantity):
    pass


class SpeedUnit(RootUnit[Speed]):
    quantity_cls = Speed


class Volume(Quantity):
    pass


class VolumeUnit(RootUnit[Volume]):
    quantity_cls = Volume


class Area(Quantity):
    pass


class AreaUnit(RootUnit[Area]):
    quantity_cls = Area


class Force(Quantity):
    pass


class ForceUnit(RootUnit[Force]):
    quantity_cls = Force


""" Basic SI units
"""

meter = DistanceUnit("m", is_si=True)
gram = MassUnit("g", is_si=True)
seconds = TimeUnit("s", is_si=True)
amp = ElectricCurrentUnit("A", is_si=True)
kelvin = TemperatureUnit("K", is_si=True)
mol = SubstanceUnit("mol", is_si=True)
candela = LuminousIntensityUnit("cd", is_si=True)  # candela unit
steradian = SteradianUnit("sr", is_si=True)


unit("km")
unit("cm")
unit("mm")
unit("kg")
scaled_unit("tonne", "kg", 1000)  # == 1Mg.

scaled_unit("min", "s", 60.0)
scaled_unit("h", "min", 60.0)
scaled_unit("day", "h", 24.0)
scaled_unit("wk", "day", 7.0)


named_unit("Hz", [], ["s"])  # hertz
named_unit("N", ["m", "kg"], ["s", "s"])  # Newton
named_unit("W", ["J"], ["s"])  # Watt
named_unit("V", ["W"], ["A"])  # Volt
named_unit("Pa", ["N"], ["m", "m"])  # pascal
named_unit("C", ["s", "A"], [])  # Coulomb
named_unit("F", ["C"], ["V"])  # Farad
named_unit("Ohm", ["V"], ["A"])
named_unit("S", ["A"], ["V"])  # Siemens
named_unit("Wb", ["V", "s"], [])  # Weber
named_unit("T", ["Wb"], ["m", "m"])  # Tesla
named_unit("H", ["Wb"], ["A"])  # Henry
named_unit("lm", ["cd", "sr"], [])  # lumen
named_unit("lx", ["lm"], ["m", "m"])  # lux
named_unit("Bq", [], ["s"])  # Becquerel
named_unit("Gy", ["J"], ["kg"])  # Gray
named_unit("Sv", ["J"], ["kg"])  # Sievert
named_unit("kat", ["mol"], ["s"])  # Katal
named_unit("J", ["N", "m"], [])  # Joule # Dangerous, 3J is a complex number

scaled_unit("kgf", "N", 9.81)
named_unit("kg/m³", ["kg"], ["m", "m", "m"])
named_unit("km/h", ["km"], ["h"])
named_unit("m/s", ["m"], ["s"])
named_unit("m/s²", ["m"], ["s", "s"])

# named_unit("As", ["A", "s"], [])
# scaled_unit("Ah", "As", 3600)

NamedComposedUnit("Ah", ComposedUnit([unit("A"), unit("h")], [], 1))

unit("dm")

named_unit("L", ["dm", "dm", "dm"], [])
named_unit("m³", ["m", "m", "m"], [])
named_unit("m²", ["m", "m"], [])

# liter = VolumeUnit.unit("L")
# square_meter = AreaUnit.unit("m²")
# cubic_meter = VolumeUnit.unit("m³")
#


# Named units

""" Mass units
"""

tonne = MassUnit.unit("tonne")
kilogram = MassUnit.unit("kg")


""" Distance units
"""

centimeter = DistanceUnit.unit("cm")
millimeter = DistanceUnit.unit("mm")
kilometer = DistanceUnit.unit("km")


""" Temporal units
"""
minutes = TimeUnit.unit("min")
hours = TimeUnit.unit("h")
days = TimeUnit.unit("day")
week = TimeUnit.unit("wk")


""" Speed/Velocity units
"""

ms = SpeedUnit.unit("m/s")
kmh = SpeedUnit.unit("km/h")

ms2 = AccelerationUnit.unit("m/s²")
""" Electrical units
"""

amphour = CurrentOverTimeUnit.unit("Ah")
volt = VoltageUnit.unit("V")

""" Force units
"""

newton = ForceUnit.unit("N")
kgf = ForceUnit.unit("kgf")

liter = VolumeUnit.unit("L")
square_meter = AreaUnit.unit("m²")
cubic_meter = VolumeUnit.unit("m³")
kg_m3 = DensityUnit.unit("kg/m³")


# These should at some point be added to a specific typed Quantity class
# """
#
#
# kg_m3 = named_unit("kg/m³", ["kg"], ["m³"])
# kmh = named_unit("km/h", ["km"], ["h"])
# ms = named_unit("m/s", ["m"], ["s"])
# newton = ForceUnit.unit("N")
# kgf = ForceUnit.unit("kgf")
