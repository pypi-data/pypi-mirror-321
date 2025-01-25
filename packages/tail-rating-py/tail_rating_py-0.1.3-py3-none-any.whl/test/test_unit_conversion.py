from enum import Enum
from datetime import datetime
from typing import Dict, Tuple
from pydantic import BaseModel
import pint

# Initialize the pint UnitRegistry
ureg = pint.UnitRegistry()

class Attribute(Enum):
    AIR_TEMPERATURE = "Air Temperature"
    RELATIVE_HUMIDITY = "Relative Humidity"
    ILLUMINANCE = "Illuminance"
    CO2 = "CO2"
    PM25 = "PM2.5"
    FORMALDEHYDE = "Formaldehyde"
    BENZENE = "Benzene"
    RADON = "Radon"
    VENTILATION_RATE = "Ventilation Rate"
    MOLD = "Mold"
    SOUND_PRESSURE_LEVEL = "Sound Pressure Level"
    DAYLIGHT_FACTOR = "Daylight Factor"

class Unit(Enum):
    CELSIUS = ureg.celsius
    FAHRENHEIT = ureg.fahrenheit
    PERCENT = ureg.percent
    LUX = ureg.lux
    PPM = ureg.ppm
    MICROGRAM_PER_CUBIC_METER = ureg.microgram / ureg.meter**3
    BECQUEREL_PER_CUBIC_METER = ureg.becquerel / ureg.meter**3
    LITERS_PER_SECOND = ureg.liter / ureg.second
    DECIBEL = ureg.decibel
    RATIO = ureg.dimensionless

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

class SensorAttribute(BaseModel):
    attribute: Attribute
    unit: Unit

    def __hash__(self):
        return hash((self.attribute, self.unit))

    def __eq__(self, other):
        if isinstance(other, SensorAttribute):
            return self.attribute == other.attribute and self.unit == other.unit
        return False

class DataPoint(BaseModel):
    timestamp: datetime
    value: Dict[SensorAttribute, float]

    def convert_to_default_units(self) -> 'DataPoint':
        converted_values = {}
        for attr, value in self.value.items():
            default_unit = DEFAULT_UNITS.get(attr.attribute)
            if default_unit and default_unit != attr.unit:
                converted_value = self.convert_unit(attr.attribute, value, attr.unit, default_unit)
            else:
                converted_value = value
            converted_values[SensorAttribute(attribute=attr.attribute, unit=default_unit)] = converted_value
        return DataPoint(timestamp=self.timestamp, value=converted_values)

    @staticmethod
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
            quantity = value * from_unit.value

        if to_unit == Unit.CELSIUS:
            # Convert Kelvin back to Celsius
            converted_value = quantity.to(ureg.kelvin).magnitude - 273.15
        elif to_unit == Unit.FAHRENHEIT:
            # Convert Kelvin back to Fahrenheit
            converted_value = (quantity.to(ureg.kelvin).magnitude - 273.15) * 9/5 + 32
        else:
            converted_value = quantity.to(to_unit.value).magnitude

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
            converted_value = quantity.to(default_unit.value).magnitude

        return converted_value
    return value

# Example usage
# Create a DataPoint
data_point = DataPoint(
    timestamp=datetime.now(),
    value={
        SensorAttribute(attribute=Attribute.AIR_TEMPERATURE, unit=Unit.CELSIUS): 23,
        SensorAttribute(attribute=Attribute.AIR_TEMPERATURE, unit=Unit.FAHRENHEIT): 73.4,
        SensorAttribute(attribute=Attribute.RELATIVE_HUMIDITY, unit=Unit.PERCENT): 35,
        SensorAttribute(attribute=Attribute.PM25, unit=Unit.MICROGRAM_PER_CUBIC_METER): 6,
        SensorAttribute(attribute=Attribute.CO2, unit=Unit.PPM): 560,
        SensorAttribute(attribute=Attribute.FORMALDEHYDE, unit=Unit.MICROGRAM_PER_CUBIC_METER): 15,
        SensorAttribute(attribute=Attribute.BENZENE, unit=Unit.MICROGRAM_PER_CUBIC_METER): 2,
        SensorAttribute(attribute=Attribute.RADON, unit=Unit.BECQUEREL_PER_CUBIC_METER): 100,
        SensorAttribute(attribute=Attribute.VENTILATION_RATE, unit=Unit.LITERS_PER_SECOND): 10,
        SensorAttribute(attribute=Attribute.SOUND_PRESSURE_LEVEL, unit=Unit.DECIBEL): 45,
        SensorAttribute(attribute=Attribute.ILLUMINANCE, unit=Unit.LUX): 250,
        SensorAttribute(attribute=Attribute.DAYLIGHT_FACTOR, unit=Unit.PERCENT): 4.5,
        # Mold is not converted as it is categorical
    }
)

# Convert to default units
converted_data_point = data_point.convert_to_default_units()
print(converted_data_point.model_dump_json(indent=2))

# Example of converting a single value
value = 73.4
from_unit = ureg.fahrenheit
attribute = Attribute.AIR_TEMPERATURE
converted_value = convert_to_default_units(value, from_unit, attribute)
print(f"Converted value: {converted_value}")
