import pint

from .model import Attribute, Unit

# Initialize the pint UnitRegistry
ureg = pint.UnitRegistry()

# Add missing unit definitions
ureg.define('ug/m3 = microgram / meter ** 3')
ureg.define('Bq/m3 = becquerel / meter ** 3')
ureg.define('L/s = liter / second')

# Default units for each attribute
DEFAULT_UNITS = {
    Attribute.AIR_TEMPERATURE: Unit.CELSIUS,
    Attribute.RELATIVE_HUMIDITY: Unit.PERCENT,
    Attribute.ILLUMINANCE: Unit.LUX,
    Attribute.CO2: Unit.PPM,
    Attribute.PM25: Unit.MICROGRAM_PER_CUBIC_METER,
    Attribute.FORMALDEHYDE: Unit.MICROGRAM_PER_CUBIC_METER,
    Attribute.BENZENE: Unit.MICROGRAM_PER_CUBIC_METER,
    Attribute.RADON: Unit.BECQUEREL_PER_CUBIC_METER,
    Attribute.VENTILATION_RATE: Unit.LITERS_PER_SECOND,
    Attribute.SOUND_PRESSURE_LEVEL: Unit.DECIBEL,
    Attribute.DAYLIGHT_FACTOR: Unit.PERCENT,
    # Mold is not converted as it is categorical
}

def convert_unit(attribute: Attribute, value: float, from_unit: Unit, to_unit: Unit) -> float:
    # Use pint for unit conversion
    if from_unit == Unit.CELSIUS:
        # Convert Celsius to Kelvin for arithmetic operations
        value_kelvin = value + 273.15
        quantity = value_kelvin * ureg.kelvin
    elif from_unit == Unit.FAHRENHEIT:
        # Convert Fahrenheit to Kelvin for arithmetic operations
        value_kelvin = (value - 32) * 5/9 + 273.15
        quantity = value_kelvin * ureg.kelvin
    else:
        quantity = value * ureg(from_unit.value)

    if to_unit == Unit.CELSIUS:
        # Convert Kelvin back to Celsius
        converted_value = quantity.to(ureg.kelvin).magnitude - 273.15
    elif to_unit == Unit.FAHRENHEIT:
        # Convert Kelvin back to Fahrenheit
        converted_value = (quantity.to(ureg.kelvin).magnitude - 273.15) * 9/5 + 32
    else:
        converted_value = quantity.to(ureg(to_unit.value)).magnitude

    return converted_value

# Function to convert ureg units into the default unit for the passed ureg units only
def convert_to_default_units(value: float, from_unit: pint.Unit, attribute: Attribute) -> float:
    default_unit = DEFAULT_UNITS.get(attribute)
    if default_unit:
        if from_unit == ureg.celsius:
            # Convert Celsius to Kelvin for arithmetic operations
            value_kelvin = value + 273.15
            quantity = value_kelvin * ureg.kelvin
        elif from_unit == ureg.fahrenheit:
            # Convert Fahrenheit to Kelvin for arithmetic operations
            value_kelvin = (value - 32) * 5/9 + 273.15
            quantity = value_kelvin * ureg.kelvin
        else:
            quantity = value * from_unit

        if default_unit == Unit.CELSIUS:
            # Convert Kelvin back to Celsius
            converted_value = quantity.to(ureg.kelvin).magnitude - 273.15
        elif default_unit == Unit.FAHRENHEIT:
            # Convert Kelvin back to Fahrenheit
            converted_value = (quantity.to(ureg.kelvin).magnitude - 273.15) * 9/5 + 32
        else:
            converted_value = quantity.to(ureg(default_unit.value)).magnitude

        return converted_value
    return value