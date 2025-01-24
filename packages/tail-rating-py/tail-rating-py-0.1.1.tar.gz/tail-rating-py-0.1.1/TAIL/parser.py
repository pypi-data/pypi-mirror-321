import pandas as pd
from datetime import datetime

from typing import List

from .model import Building, Room, SensorData, DataPoint, Record, SensorAttribute, Attribute, Unit, RoomType, BuildingType, Mold

def parse_original_csv(file_path: str) -> List[Building]:
    df = pd.read_csv(file_path)

    building_names = df['building'].unique()

    buildings = []

    for building_name in building_names:
        df_building = df[df['building'] == building_name]
        # Occupancy is equal to the sum of the occupants in each room
        merge_df = df_building.groupby('room').agg({
            'occupancy': 'first',
            'floorArea': 'first',
            }).reset_index()
        occupancy = merge_df['occupancy'].sum().astype(float)
        floor_area = merge_df['floorArea'].sum().astype(float)

        rooms = df_building['room'].unique()

        if "buildingType" in df_building.columns:
            buildingType = df_building['buildingType'].unique()
            if len(buildingType) > 1:
                raise ValueError("Multiple building types found for the same building")
            else:
                buildingType = sanitize_name(buildingType[0])
                # Check is buildintType is valid
                if buildingType not in BuildingType.__members__:
                    raise ValueError(f"Invalid building type: {buildingType}")
                else:
                    buildingType = BuildingType[buildingType]
        else:
            buildingType = BuildingType.OFFICE
        
        building = Building(
            name=building_name,
            buildingType=buildingType,
            floorArea=floor_area,
            occupants=occupancy,
            rooms=[],
            coordinates="0,0"
        )

        for room in rooms:
            df_room = df_building[df_building['room'] == room]
            room_floor_area = df_room['floorArea'].unique()[0]
            room_occupants = df_room['occupancy'].unique()[0]
            room_type = df_room['roomType'].unique()
            if len(room_type) > 1:
                raise ValueError("Multiple room types found for the same room")
            else:
                room_type = sanitize_name(room_type[0])
                # Check if roomType is valid
                if room_type not in RoomType.__members__:
                    raise ValueError(f"Invalid room type: {room_type}")
                else:
                    room_type = RoomType[room_type]

            sensors = []
            # Create a dict of sensor name and sensor data
            dict_sensor = df_room.groupby('sensor').agg({
                'timestamp': list,
                'parameter': list,
                'value': list,
                'unit': list
            }).reset_index()

            dict_sensor = dict_sensor.to_dict(orient='records')

            for sensor in dict_sensor:
                # Create on sensor by sensor name
                sensor_name = sensor['sensor']
                # from the other columns create a df
                df_sensor = pd.DataFrame({
                    'timestamp': sensor['timestamp'],
                    'parameter': sensor['parameter'],
                    'value': sensor['value'],
                    'unit': sensor['unit']
                })
                # Group by timestamp
                df_sensor['timestamp'] = pd.to_datetime(df_sensor['timestamp'], dayfirst=True)
                df_sensor = df_sensor.groupby('timestamp').agg({
                    'parameter': list,
                    'value': list,
                    'unit': list
                }).reset_index()

                data_points = []
                attributes = set()
                for index, row in df_sensor.iterrows():
                    records = []
                    for i in range(len(row['parameter'])):
                        attributes.add(SensorAttribute(
                            attribute=Attribute[sanitize_name(row['parameter'][i])],
                            unit=Unit[sanitize_name(row['unit'][i])]
                        ))
                        records.append(Record(
                            sensorAttr=SensorAttribute(
                                attribute=Attribute[sanitize_name(row['parameter'][i])],
                                unit=Unit[sanitize_name(row['unit'][i])]
                            ),
                            value=row['value'][i] if Attribute[sanitize_name(row['parameter'][i])] != Attribute.MOLD else Mold[row['value'][i]]
                        ))
                    data_points.append(DataPoint(
                        timestamp=row['timestamp'],
                        records=records
                    ))

                sensors.append(SensorData(
                    sensorName=sensor_name,
                    attributes=list(attributes),
                    data=data_points
                ))

            room_obj = Room(
                name=room,
                floorArea=room_floor_area,
                occupants=room_occupants,
                roomType=room_type,
                sensors=sensors
            )

            building.add_room(room_obj)
        
        buildings.append(building)

    return buildings


def sanitize_name(name: str) -> str:
    return name.strip().replace(" ", "_").upper()