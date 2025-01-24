from enum import Enum
from datetime import datetime
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict
from uuid import uuid4
import pandas as pd
import pickle
import numpy as np

from .schedule import YearSchedule

class Quality(Enum):
    EXCELLENT = 1
    GOOD = 2
    FAIR = 3
    POOR = 4

    @staticmethod
    def average(qualities: List['Quality']) -> 'Quality':
        return Quality(np.ceil(np.mean([q.value for q in qualities])).astype(int))
    
    # Add a method to compare the quality of two objects
    def __lt__(self, other: 'Quality') -> bool:
        return self.value < other.value
    
    def __le__(self, other: 'Quality') -> bool:
        return self.value <= other.value
    
    def __gt__(self, other: 'Quality') -> bool:
        return self.value > other.value
    
    def __ge__(self, other: 'Quality') -> bool:
        return self.value >= other.value
    
    def __eq__(self, other: 'Quality') -> bool:
        return self.value == other.value
    
    def __ne__(self, other: 'Quality') -> bool:
        return self.value != other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        return f'{self.name}'

class BuildingType(Enum):
    RESIDENTIAL = "Residential"
    HOTEL = "Hotel"
    OFFICE = "Office"
    MIXED_USE = "Mixed Use"
    EDUCATIONAL = "Educational"

class Building(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={pd.DataFrame: lambda df: df.to_dict()})
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    floorArea: float
    occupants: int
    buildingType: BuildingType
    coordinates: str
    schedule: Optional['YearSchedule'] = None
    rooms: List['Room'] = []
    tail_rating: Optional['TAILRating'] = None

    def add_schedule(self, schedule: 'YearSchedule'):
        self.schedule = schedule
        for room in self.rooms:
            if room.schedule is None or room.default_building_schedule:
                room.assign_building_schedule()
            for sensor in room.sensors:
                if sensor.schedule is None or sensor.default_building_schedule:
                    sensor.assign_building_schedule()

    def add_room(self, room: 'Room'):
        if room not in self.rooms:
            self.rooms.append(room)
    
    def to_pickle(self, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            
    @staticmethod
    def from_pickle(filename: str) -> 'Building':
        with open(filename, 'rb') as f:
            return pickle.load(f)

class PollutionLevel(Enum):
    VERY_LOW_EMISSION = "Very Low Emission"
    LOW_EMISSION = "Low Emission"
    NON_LOW_EMISSION = "Non-Low Emission"

class TAIL(BaseModel):
    attributes: Dict['Attribute', Quality] = Field(default_factory=dict)
    indicators: Dict['Indicator', Quality] = Field(default_factory=dict)
    overall: Optional[Quality] = None

    def calculate_overall(self):
        self.overall = max((quality for quality in self.indicators.values() if quality is not None), default=None)

    def assign_indicator(self, indicator: 'Indicator', quality: Quality):
        self.indicators[indicator] = quality

    def assign_all_attributes(self, attributes: Dict['Attribute', Quality]):
        self.attributes = attributes

class Room(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={pd.DataFrame: lambda df: df.to_dict()})
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    floorArea: float
    occupants: int
    pollutionLevel: PollutionLevel = PollutionLevel.NON_LOW_EMISSION
    roomType: 'RoomType'
    schedule: Optional['YearSchedule'] = None
    default_building_schedule: bool = False
    sensors: Optional[List['SensorData']] = Field(default_factory=list)
    room_df: Optional[pd.DataFrame] = None
    tail: 'TAIL' = Field(default_factory=TAIL)

    def __init__(self, **data):
        super().__init__(**data)
        self.tail = TAIL()

    def assign_building_schedule(self):
        self.default_building_schedule = True

    def add_schedule(self, schedule: 'YearSchedule'):
        self.schedule = schedule

    def add_sensor(self, sensor: 'SensorData'):
        if sensor not in self.sensors:
            self.sensors.append(sensor)
            sensor.add_room_id(self)
    
    def frame_data(self):
        self.room_df = create_sensor_df(self.sensors)
        return self.room_df
    
    def add_quality_for_attribute(self, attribute: 'Attribute', quality: Quality):
        self.tail.attributes[attribute] = quality

class SensorData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={pd.DataFrame: lambda df: df.to_dict()})
    id: str = Field(default_factory=lambda: str(uuid4()))
    sensorName: str
    attributes: List['SensorAttribute']
    data: List['DataPoint']
    schedule: Optional['YearSchedule'] = None
    default_building_schedule: bool = False
    sensor_df: Optional[pd.DataFrame] = None
    quality: Optional[Dict['Attribute', Quality]] = Field(default_factory=dict)
    rooms_id: Optional[List[str]] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        self.quality = {}

    def assign_building_schedule(self):
        self.default_building_schedule = True

    def add_schedule(self, schedule: 'YearSchedule'):
        self.schedule = schedule

    def add_room_id(self, room: Room):
        if room.id not in self.rooms_id:
            self.rooms_id.append(room.id)
        
    def frame_data(self):
        self.sensor_df = create_sensor_df([self])
        return self.sensor_df
    
    def add_quality_for_attribute(self, attribute: 'Attribute', quality: Quality, room: Room = None):
        self.quality[attribute] = quality
        if room is not None:
            room.add_quality_for_attribute(attribute, quality)

class RoomType(Enum):
    SMALL_OFFICE = "Single Office"
    OPEN_PLAN_OFFICE = "Open Plan Office"
    HOTEL_ROOM = "Hotel Room"
    CONFERENCE_ROOM = "Conference Room"
    CLASSROOM = "Classroom"
    LECTURE_HALL = "Lecture Hall"
    LIBRARY = "Library"
    AUDITORIUM = "Auditorium"
    GYM = "Gym"
    RESTAURANT = "Restaurant"
    KITCHEN = "Kitchen"

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

    @classmethod
    def list(cls):
        return list(cls)

class Mold(Enum):
    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Unit(Enum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    PERCENT = "percent"
    LUX = "lux"
    PPM = "ppm"
    MICROGRAM_PER_CUBIC_METER = "ug/m3"
    BECQUEREL_PER_CUBIC_METER = "Bq/m3"
    LITERS_PER_SECOND = "L/s"
    DECIBEL = "dB(A)"
    RATIO = "ratio"
    CAT = "cat"

class SensorAttribute(BaseModel):
    attribute: Attribute
    unit: Unit
    
    def __hash__(self):
        return hash((self.attribute, self.unit))

    def __eq__(self, other):
        if isinstance(other, SensorAttribute):
            return self.attribute == other.attribute and self.unit == other.unit
        return False

class Record(BaseModel):
    sensorAttr: SensorAttribute
    value: Union[float, Mold, int]

    def is_valid(self) -> bool:
        if self.sensorAttr.attribute == Attribute.MOLD:
            return isinstance(self.value, Mold)
        return isinstance(self.value, (float, int))

class DataPoint(BaseModel):
    timestamp: datetime
    records: List[Record]

    def convert_to_default_units(self) -> 'DataPoint':
        from .units import convert_unit
        converted_values = {}
        for record in self.records:
            if record.sensorAttr.attribute in DEFAULT_UNITS:
                converted_values[record.sensorAttr] = convert_unit(record.value, record.sensorAttr.unit, DEFAULT_UNITS[record.sensorAttr.attribute])
            else:
                converted_values[record.sensorAttr] = record.value
        return DataPoint(timestamp=self.timestamp, records=[Record(sensorAttr=attr, value=val) for attr, val in converted_values.items()])

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
}

class Indicator(Enum):
    THERMAL = "Thermal"
    ACOUSTIC = "Acoustic"
    INDOOR_AIR_QUALITY = "Indoor Air Quality"
    LIGHTING = "Lighting"

    @classmethod
    def list(cls):
        return list(cls)

class TAIL(BaseModel):
    attributes: Dict[Attribute, Quality] = Field(default_factory=dict)
    indicators: Dict[Indicator, Quality] = Field(default_factory=dict)
    overall: Optional[Quality] = None

    def calculate_overall(self):
        self.overall = max((quality for quality in self.indicators.values() if quality is not None), default=None)

    def assign_indicator(self, indicator: Indicator, quality: Quality):
        self.indicators[indicator] = quality

    def assign_all_attributes(self, attributes: Dict[Attribute, Quality]):
        self.attributes = attributes

class TAILRating(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    from_date: datetime
    to_date: datetime
    tail: Optional[TAIL]
    name: str
    building_id: str
    rooms_id: Optional[List[str]] = Field(default_factory=list)
    sensors_id: Optional[List[str]] = Field(default_factory=list)
    valid: bool = True
    valid_until: Optional[datetime] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.valid_until = self.valid_until or self.from_date.replace(year=self.from_date.year + 1)
        
    def add_room_id(self, room: Room):
        if room.id not in self.rooms_id:
            self.rooms_id.append(room.id)

    def add_sensor_id(self, sensor: SensorData):
        if sensor.id not in self.sensors_id:
            self.sensors_id.append(sensor.id)

    def invalidate(self):
        self.valid = False
        self.valid_until = datetime.now()

def create_sensor_df(sensor_data: List[SensorData]) -> pd.DataFrame:
    data = []
    for sensor in sensor_data:
        for dataPoint in sensor.data:
            row = {'timestamp': dataPoint.timestamp}
            for record in dataPoint.records:
                row[record.sensorAttr.attribute] = record.value
            data.append(row)

    df = pd.DataFrame(data)
    df.set_index('timestamp', inplace=True)
    df.index = df.index.round('s')
    df = df.groupby(df.index).agg(lambda x: x.mean() if x.dtype.kind in 'biufc' else (x.mode().iat[0] if not x.mode().empty else np.nan))
    df.sort_index(inplace=True)

    return df
