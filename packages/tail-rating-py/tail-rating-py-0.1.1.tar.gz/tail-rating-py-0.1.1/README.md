# TAIL-Rating-Py

TAIL-Rating-Py is a Python package designed to assess TAIL (Thermal, Acoustic, Indoor Air Quality, and Lighting) for buildings. The package provides data models and functions to facilitate the TAIL project.

It follows the development made by Prof. Pawel Wargocki and his team at the International Centre for Indoor Environment and Energy, Technical University of Denmark.

The package includes the following modules:
- `model`: Contains the data models for buildings, rooms, sensor data, data points, and sensor attributes.
- `parser`: Contains functions to parse sensor data from CSV files.
- `categorise`: Contains functions to categorise buildings and rooms based on sensor data.
- `tail`: Contains functions to assign TAIL ratings to buildings and rooms.
- `dummy_data`: Contains functions to create dummy data for testing purposes.

## Installation

To install the package, run:
```sh
pip install tail-rating-py
```

## Data Models

### Building

The `Building` model represents a building in the TAIL project. It includes attributes such as `id`, `name`, `floorArea`, `occupants`, `buildingType`, `coordinates`, `schedule`, `rooms`, and `tail_rating`.

### Room

The `Room` model represents a room within a building. It includes attributes such as `id`, `name`, `floorArea`, `occupants`, `pollutionLevel`, `roomType`, `schedule`, `sensors`, `room_df`, and `tail`.

### SensorData

The `SensorData` model represents data collected by a sensor. It includes attributes such as `id`, `sensorName`, `attributes`, `data`, `schedule`, `sensor_df`, and `quality`.

### DataPoint and SensorAttribute

The `DataPoint` model represents a data point collected by a sensor. It includes attributes such as `timestamp` and `records`.

The `SensorAttribute` model represents the attributes that can be collected by sensors, such as `AIR_TEMPERATURE`, `RELATIVE_HUMIDITY`, `ILLUMINANCE`, etc.

## Example Usage

Here's an example of how to create and use these models:

```python
from datetime import datetime
from TAIL.model import Building, BuildingType, Room, SensorData, DataPoint, SensorAttribute, Attribute, Unit

# Create a Building
building = Building(
    name="Office Building",
    floorArea=1000.0,
    occupants=50,
    buildingType=BuildingType.OFFICE,
    coordinates="40.7128° N, 74.0060° W"
)

# Create a Room
room = Room(
    name="Conference Room",
    floorArea=50.0,
    occupants=10,
    roomType="Conference",
    building=building
)

# Create a SensorAttribute
sensor_attribute = SensorAttribute(
    attribute=Attribute.AIR_TEMPERATURE, 
    unit=Unit.CELSIUS
)

# Create a DataPoint
data_point = DataPoint(
    timestamp=datetime.now(),
    records=[{"sensorAttr": sensor_attribute, "value": 23.0}]
)

# Create SensorData
sensor_data = SensorData(
    sensorName="Temperature Sensor",
    attributes=[sensor_attribute],
    data=[data_point],
    room=room
)

# Add the room to the building
building.add_room(room)

# Add the sensor data to the room
room.add_sensor(sensor_data)

# Print the building
print(building.model_dump_json(indent=2))
```

## Assessing TAIL for Buildings

This guide explains how to assess TAIL for buildings using the provided Python code.

### Steps to Assess TAIL

1. **Create the Building Model**

   Use the `parse_original_csv` function to create the building model from a CSV file containing sensor data.

   ```python
   from TAIL.parser import parse_original_csv

   building = parse_original_csv("weekly_sensor_data.csv")
   ```

2. **Categorise the Building Model**

   Categorise the building model using the `categorise` function.

   ```python
   from TAIL.categorise import categorise

   building = categorise(building[0])
   ```

3. **Assign TAIL Ratings to the Rooms**

   Assign TAIL ratings to the rooms in the building using the `assign_tail_rating` function.

   ```python
   from TAIL.tail import assign_tail_rating

   building = assign_tail_rating(building)
   ```

4. **Assign TAIL Rating to the Building**

   Assign an overall TAIL rating to the building using the `assign_tail_rating_to_building` function.

   ```python
   from TAIL.tail import assign_tail_rating_to_building

   building = assign_tail_rating_to_building(building)
   ```

5. **Print the Building Model**

   Print the building model in JSON format.

   ```python
   print(building.model_dump_json(indent=2))
   ```

6. **Save the Building Model to a File**

   Save the building model to a file in JSON format.

   ```python
   with open('building_model.json', 'w') as f:
       f.write(building.model_dump_json(indent=2))
   ```

### Example Usage in a Script

Here's an example of how you might use these steps in a script:

```python
# %% Import necessary functions
from TAIL.dummy_data import create_building_model
from TAIL.categorise import categorise
from TAIL.tail import assign_tail_rating, assign_tail_rating_to_building
from TAIL.parser import parse_original_csv

# %% Create the building model
building = parse_original_csv("weekly_sensor_data.csv")

# %% Categorise the building model
building = categorise(building[0])

# %% Assign TAIL ratings to the rooms in the building
building = assign_tail_rating(building)

# %% Assign TAIL rating to the building
building = assign_tail_rating_to_building(building)

# %% Print the building model
print(building.model_dump_json(indent=2))

# %% Save the building model to a file in JSON format
with open('building_model.json', 'w') as f:
    f.write(building.model_dump_json(indent=2))
```

This example demonstrates how to create a building model from sensor data, categorise it, assign TAIL ratings, and save the results.

## License
GNU General Public License v3.0

## Future development
- [ ] Add the graphical representation of the TAIL ratings.
- [ ] Improve the categorisation and rating at the building level based on the original script.
- [ ] Implement more roomType, buildingType
- [ ] Improve the documentation and examples.
- [ ] Clean the code and improve the performance.