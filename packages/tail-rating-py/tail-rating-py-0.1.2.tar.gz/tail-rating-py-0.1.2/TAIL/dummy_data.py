from datetime import datetime, timedelta
from .model import Building, Room, SensorData, DataPoint, SensorAttribute, Attribute, Unit, BuildingType, Record, RoomType, Mold

import random

from .schedule import create_basic_schedule

# Create some fake data points
def create_fake_data_points(attributes):
    data_points = []
    from_date = datetime(2025, 1, 1, 0, 0)
    to_date = datetime(2025, 1, 31, 23, 30)
    timestep = timedelta(minutes=30)
    
    # Create a list of timestamps
    timestamps = [from_date + i * timestep for i in range(int((to_date - from_date) / timestep))]   

    # Create a list of records for each timestamp, create a random value for each sensor attribute
    for timestamp in timestamps:
        records = [Record(sensorAttr=attribute, value=random.uniform(0, 100)) for attribute in attributes if attribute.attribute != Attribute.MOLD]
        
        # For SensorAttribute that contains attribute Mold, we need to assign a random value from the Mold enum:
        if any(attribute.attribute == Attribute.MOLD for attribute in attributes):
            records.append(Record(sensorAttr=SensorAttribute(attribute=Attribute.MOLD, unit=Unit.CAT), value=Mold(random.choice([Mold.NONE, Mold.LOW, Mold.MEDIUM, Mold.HIGH]))))

        
        data_points.append(DataPoint(timestamp=timestamp, records=records))

    return data_points

def create_building_model() -> Building:
    # Create sensor attributes
    sensor_attributes_1 = [
        SensorAttribute(attribute=Attribute.AIR_TEMPERATURE, unit=Unit.CELSIUS),
        SensorAttribute(attribute=Attribute.RELATIVE_HUMIDITY, unit=Unit.PERCENT),
    ]

    sensor_one_time_measurements = [
        SensorAttribute(attribute=Attribute.ILLUMINANCE, unit=Unit.LUX),
        SensorAttribute(attribute=Attribute.SOUND_PRESSURE_LEVEL, unit=Unit.DECIBEL),
        SensorAttribute(attribute=Attribute.DAYLIGHT_FACTOR, unit=Unit.PERCENT),
        SensorAttribute(attribute=Attribute.MOLD, unit=Unit.CAT)
    ]

    sensor_attributes_2 = [
        SensorAttribute(attribute=Attribute.CO2, unit=Unit.PPM),
        SensorAttribute(attribute=Attribute.PM25, unit=Unit.MICROGRAM_PER_CUBIC_METER)
    ]

    # Create sensors
    sensor_1 = SensorData(sensorName="Sensor 1", attributes=sensor_attributes_1, data=create_fake_data_points(sensor_attributes_1))
    sensor_2 = SensorData(sensorName="Sensor 2", attributes=sensor_attributes_2, data=create_fake_data_points(sensor_attributes_2))

    sensor_3 = SensorData(sensorName="Sensor 3", attributes=sensor_attributes_1, data=create_fake_data_points(sensor_attributes_1))
    sensor_4 = SensorData(sensorName="Sensor 4", attributes=sensor_attributes_2, data=create_fake_data_points(sensor_attributes_2))

    sensor_5 = SensorData(sensorName="Sensor 5", attributes=sensor_one_time_measurements, data=create_fake_data_points(sensor_one_time_measurements))

    # Create rooms
    room_1 = Room(name="Room 1", floorArea=50.0, occupants=5, roomType=RoomType.SMALL_OFFICE)
    room_2 = Room(name="Room 2", floorArea=75.0, occupants=10, roomType=RoomType.HOTEL_ROOM, sensors=[sensor_3, sensor_4, sensor_5])

    room_1.add_sensor(sensor_1)
    room_1.add_sensor(sensor_2)
    room_1.add_sensor(sensor_5)

    # Save the data using pickle
    building = Building(name="Building 0", floorArea=500.0, occupants=50, buildingType=BuildingType.OFFICE, coordinates="0,0", rooms=[room_1, room_2])

    # Create a schedule for the building
    schedule = create_basic_schedule(2025, "DK")
    building.add_schedule(schedule)

    return building
