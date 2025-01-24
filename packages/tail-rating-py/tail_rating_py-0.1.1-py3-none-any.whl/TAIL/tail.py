# Description: This file contains the TAIL object and the function that assigns the TAIL object to the rooms, sensors and buildings
from .model import Room, Building, Attribute, Indicator, TAIL, TAILRating, Quality
from typing import Dict, List

## CONSTANTS ##
THERMAL = {Attribute.AIR_TEMPERATURE}
ACOUSTIC = {Attribute.SOUND_PRESSURE_LEVEL}
INDOOR_AIR_QUALITY = {
    Attribute.CO2, Attribute.RELATIVE_HUMIDITY, Attribute.BENZENE, Attribute.FORMALDEHYDE, Attribute.PM25, Attribute.RADON, Attribute.VENTILATION_RATE, Attribute.MOLD
}
LIGHTING = {Attribute.ILLUMINANCE, Attribute.DAYLIGHT_FACTOR}

TAIL_INDICATORS = {
    Indicator.THERMAL: THERMAL,
    Indicator.ACOUSTIC: ACOUSTIC,
    Indicator.INDOOR_AIR_QUALITY: INDOOR_AIR_QUALITY,
    Indicator.LIGHTING: LIGHTING
}

## FUNCTIONS ##
def get_tail_rating(room: Room) -> TAIL:
    """
    Get the worst quality for each TAIL indicator in the room.
    """

    for tail_indicator, attributes in TAIL_INDICATORS.items():
        quality = max((room.tail.attributes[attr] for attr in attributes if attr in room.tail.attributes), default=None)
        room.tail.assign_indicator(tail_indicator, quality)

    room.tail.calculate_overall()
    return room

def assign_tail_rating(building: Building) -> Building:
    """
    Assign TAIL rating to each room in the building.
    """
    for room in building.rooms:
        room = get_tail_rating(room)
    return building

def assign_tail_rating_to_building(building: Building) -> Building:
    """
    Take the average of the TAIL ratings of all rooms in the building and assign it to the building.
    """
    if not all(hasattr(room, 'tail') for room in building.rooms):
        raise ValueError("All rooms in the building must have a TAIL rating assigned before assigning to the building")
    
    tail = TAIL()
    attr_quality: Dict[Attribute, List[Quality]] = {}
    indicator_quality: Dict[Indicator, List[Quality]] = {}

    for room in building.rooms:
        for attr in Attribute.list():
            if attr in room.tail.attributes:
                attr_quality.setdefault(attr, []).append(room.tail.attributes[attr])
        for indicator in Indicator.list():
            if indicator in room.tail.indicators:
                indicator_quality.setdefault(indicator, []).append(room.tail.indicators[indicator])

    for attr in Attribute.list():
        tail.attributes[attr] = Quality.average(attr_quality[attr]) if attr in attr_quality else None
    for indicator in Indicator.list():
        tail.indicators[indicator] = Quality.average(indicator_quality[indicator]) if indicator in indicator_quality else None

    tail.calculate_overall()

    from_date = min(room.room_df.index.min() for room in building.rooms)
    to_date = max(room.room_df.index.max() for room in building.rooms)

    building.tail_rating = TAILRating(
        from_date=from_date,
        to_date=to_date,
        tail=tail,
        name=f"{building.name} TAIL Rating from {from_date} to {to_date}",
        building_id=building.id,
        rooms_id=[room.id for room in building.rooms],
        sensors_id=[sensor.id for room in building.rooms for sensor in room.sensors],
        valid=True
    )
        
    return building
