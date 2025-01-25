import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List

from .model import Building, SensorData, Attribute, BuildingType, Quality, Mold, RoomType
from . import const
from .ventilation import get_ventilation_rates
from .schedule import convert_to_series

def get_quality_for_attr(series: pd.Series, attribute: Attribute) -> Quality:
    # MORE STRICT IMPLEMENTATION ON SOME ATTRIBUTES
    if attribute in [Attribute.MOLD, Attribute.BENZENE, Attribute.FORMALDEHYDE, Attribute.CO2, Attribute.RADON]:
        if Quality.POOR in series.value_counts().index:
            return Quality.POOR
        elif Quality.FAIR in series.value_counts().index:
            return Quality.FAIR
        elif Quality.GOOD in series.value_counts().index:
            return Quality.GOOD
        elif Quality.EXCELLENT in series.value_counts().index:
            return Quality.EXCELLENT
        else:
            return np.nan
    else:
        freq = series.value_counts(normalize=True)
        return np.select(
                    [
                        (freq.get(Quality.EXCELLENT, 0) >= 0.94) & 
                        (freq.get(Quality.FAIR, 0) <= 0.01) &
                        (freq.get(Quality.POOR, 0) == 0),

                        (freq.get(Quality.GOOD, 0) > 0.05) &
                        (freq.get(Quality.FAIR, 0) <= 0.05) &
                        (freq.get(Quality.POOR, 0) <= 0.01),

                        (freq.get(Quality.FAIR, 0) > 0.05) &
                        (freq.get(Quality.POOR, 0) <= 0.05),

                    ],
                    [
                        Quality.EXCELLENT,
                        Quality.GOOD,
                        Quality.FAIR
                    ],
                    default=Quality.POOR
                ).item()

def categorise(building: Building, agg_level: str = 'room') -> Building:
    """
    Categorise the sensor data in the building object
    agg_level can be room or sensor depending on the level of aggregation
    """
    if agg_level not in ['room', 'sensor']:
        raise ValueError("agg_level must be either 'room' or 'sensor'")

    # TODO: IMPLEMENT BUILDING LEVEL CATEGORISATION
    
    # Iterate either over the rooms or sensors in the building
    if agg_level == 'room':
        iterable = building.rooms
    elif agg_level == 'sensor':
        iterable = [sensor for room in building.rooms for sensor in room.sensors]

    for itr in iterable:
        # Get the ventilation rates for the room
        if agg_level == 'room':
            rooms = [itr]
            ventilation_rates = [get_ventilation_rates(room=itr)]
        elif agg_level == 'sensor':
            # Check if rooms_id is empty
            if not itr.rooms_id:
                raise ValueError("Sensor must be assigned to a room")
            # Retrieve the room object from the building object using the room_id
            rooms = [room for room in building.rooms if room.id in itr.rooms_id]
            if not rooms:
                raise ValueError("Room not found in building")
            ventilation_rates = [get_ventilation_rates(room=room) for room in rooms]

        # Get the sensor into a dataframe
        measurements_df = itr.frame_data()

        # If itr.default_building_schedule is True or schedule is not None, then we can use the schedule to categorise the data
        schedule = building.schedule if itr.default_building_schedule else itr.schedule if itr.schedule else None

        if schedule is not None:
            # Convert the schedule to a pandas series
            schedule_series = convert_to_series(schedule)

            # Apply the closest schedule value to the measurements 
            schedule_series = schedule_series.reindex(measurements_df.index, method='nearest')
            # Add the schedule values to the measurements_df
            measurements_df = pd.concat([measurements_df, schedule_series], axis=1)
            measurements_df.columns = list(measurements_df.columns)[:-1] + ['Schedule']

            # Apply a boolean mask to the measurements_df to get the measurements for the row that have a schedule value > 0
            measurements_df = measurements_df[measurements_df['Schedule'] > 0]
            measurements_df.drop('Schedule', axis=1, inplace=True)

        measurements_df['Season'] = measurements_df.index.month.map(lambda x: 'Heating' if x in [10,11,12,1,2,3,4,5] else 'Non-heating')

        if Attribute.AIR_TEMPERATURE in measurements_df.columns:
            quality_series = measurements_df.apply(
                lambda row: (
                    Quality.EXCELLENT if 21 <= row[Attribute.AIR_TEMPERATURE] <= 23 else
                    Quality.GOOD if (20 <= row[Attribute.AIR_TEMPERATURE] < 21) or (23 < row[Attribute.AIR_TEMPERATURE] <= 24) else
                    Quality.FAIR if (19 <= row[Attribute.AIR_TEMPERATURE] < 20) or (24 < row[Attribute.AIR_TEMPERATURE] <= 25) else
                    Quality.POOR
                ) if row['Season'] == 'Heating' else (
                    Quality.EXCELLENT if 23.5 <= row[Attribute.AIR_TEMPERATURE] <= 25.5 else
                    Quality.GOOD if (23 <= row[Attribute.AIR_TEMPERATURE] < 23.5) or (25.5 < row[Attribute.AIR_TEMPERATURE] <= 26) else
                    Quality.FAIR if (22 <= row[Attribute.AIR_TEMPERATURE] < 23) or (26 < row[Attribute.AIR_TEMPERATURE] <= 27) else
                    Quality.POOR
                ),
                axis=1
            )

            itr.add_quality_for_attribute(attribute=Attribute.AIR_TEMPERATURE, quality=get_quality_for_attr(quality_series, Attribute.AIR_TEMPERATURE))

        if Attribute.RELATIVE_HUMIDITY in measurements_df.columns:
            if building.buildingType == BuildingType.OFFICE:
                quality_series = measurements_df.apply(
                    lambda row: (
                        Quality.EXCELLENT if 30 <= row[Attribute.RELATIVE_HUMIDITY] <= 50 else
                        Quality.GOOD if (25 <= row[Attribute.RELATIVE_HUMIDITY] < 30) or (50 < row[Attribute.RELATIVE_HUMIDITY] <= 60) else
                        Quality.FAIR if (20 <= row[Attribute.RELATIVE_HUMIDITY] < 25) or (60 < row[Attribute.RELATIVE_HUMIDITY] <= 70) else
                        Quality.POOR
                    ),
                    axis=1
                )

                itr.add_quality_for_attribute(attribute=Attribute.RELATIVE_HUMIDITY, quality=get_quality_for_attr(quality_series, Attribute.RELATIVE_HUMIDITY))

            elif building.buildingType == BuildingType.HOTEL:
                quality_series = measurements_df.apply(
                    lambda row: (
                        Quality.EXCELLENT if 30 <= row[Attribute.RELATIVE_HUMIDITY] <= 50 else
                        Quality.GOOD if (25 <= row[Attribute.RELATIVE_HUMIDITY] < 30) or (50 < row[Attribute.RELATIVE_HUMIDITY] <= 60) else
                        Quality.FAIR if 20 <= row[Attribute.RELATIVE_HUMIDITY] < 25 else
                        Quality.POOR
                    ),
                    axis=1
                )

                itr.add_quality_for_attribute(attribute=Attribute.RELATIVE_HUMIDITY, quality=get_quality_for_attr(quality_series, Attribute.RELATIVE_HUMIDITY))

            else:
                # Warn that the building type is not implemented
                print(f"Building type {building.buildingType} is not implemented for relative humidity categorisation")

        if Attribute.PM25 in measurements_df.columns:
            pm25_df = measurements_df[Attribute.PM25].copy()
            # If negative value, set to NaN
            pm25_df[pm25_df < 0] = np.nan
            # Set values below 1 to 0
            pm25_df[pm25_df < 1] = 0
            # Round to nearest whole number
            pm25_df = pm25_df.round()
            quality_series = pm25_df.map(
                lambda x: (
                    Quality.EXCELLENT if x < 10 else
                    Quality.FAIR if x > 25 else
                    Quality.POOR
                )
            )

            itr.add_quality_for_attribute(attribute=Attribute.PM25, quality=get_quality_for_attr(quality_series, Attribute.PM25))

        if Attribute.FORMALDEHYDE in measurements_df.columns:
            formaldehyde_df = measurements_df[Attribute.FORMALDEHYDE].copy()
            # If negative value, set to NaN
            formaldehyde_df[formaldehyde_df < 0] = np.nan
            # Set values below 1 to 0
            formaldehyde_df[formaldehyde_df < 1] = 0
            # Round to nearest whole number
            formaldehyde_df = formaldehyde_df.round()
            quality_series = formaldehyde_df.map(
                lambda x: (
                    Quality.EXCELLENT if x < 30 else
                    Quality.FAIR if x > 100 else
                    Quality.POOR
                ),
            )

            itr.add_quality_for_attribute(attribute=Attribute.FORMALDEHYDE, quality=get_quality_for_attr(quality_series, Attribute.FORMALDEHYDE))

        if Attribute.BENZENE in measurements_df.columns:
            benzene_df = measurements_df[Attribute.BENZENE].copy()
            # If negative value, set to NaN
            benzene_df[benzene_df < 0] = np.nan
            # Set values below 1 to 0
            benzene_df[benzene_df < 1] = 0
            # Round to nearest whole number
            benzene_df = benzene_df.round()
            quality_series = benzene_df.map(
                lambda x: (
                    Quality.EXCELLENT if x < 2 else
                    Quality.FAIR if x >= 5 else
                    Quality.POOR
                ),
            )

            itr.add_quality_for_attribute(attribute=Attribute.BENZENE, quality=get_quality_for_attr(quality_series, Attribute.BENZENE))

        if Attribute.RADON in measurements_df.columns:
            radon_df = measurements_df[Attribute.RADON].copy()
            # If negative value, set to NaN
            radon_df[radon_df < 0] = np.nan
            # Set values below 1 to 0
            radon_df[radon_df < 1] = 0
            # Round to nearest whole number
            radon_df = radon_df.round()
            quality_series = radon_df.map(
                lambda x: (
                    Quality.EXCELLENT if x < 100 else
                    Quality.FAIR if x > 300 else
                    Quality.POOR
                ),
            )

            itr.add_quality_for_attribute(attribute=Attribute.RADON, quality=get_quality_for_attr(quality_series, Attribute.RADON))

        if Attribute.VENTILATION_RATE in measurements_df.columns:
            ventilation_rates = ventilation_rates[0] # TODO: NEED TO IMPLEMENT FOR MULTIPLE ROOMS WITH SAME SENSOR
            quality_series = measurements_df.apply(
                lambda row: (
                    Quality.EXCELLENT if row[Attribute.VENTILATION_RATE] >= ventilation_rates[Quality.EXCELLENT] else
                    Quality.GOOD if (ventilation_rates[Quality.GOOD] <= row[Attribute.VENTILATION_RATE] < ventilation_rates[Quality.EXCELLENT]) else
                    Quality.FAIR if (ventilation_rates[Quality.FAIR] <= row[Attribute.VENTILATION_RATE] < ventilation_rates[Quality.GOOD]) else
                    Quality.POOR
                ),
                axis=1
            )

            itr.add_quality_for_attribute(attribute=Attribute.VENTILATION_RATE, quality=get_quality_for_attr(quality_series, Attribute.VENTILATION_RATE))

        if Attribute.MOLD in measurements_df.columns:
            quality_series = measurements_df.apply(
                lambda row: (
                    Quality.EXCELLENT if row[Attribute.MOLD] == Mold.NONE else
                    Quality.GOOD if row[Attribute.MOLD] == Mold.LOW else
                    Quality.FAIR if row[Attribute.MOLD] == Mold.MEDIUM else
                    Quality.POOR
                ),
                axis=1
            )

            itr.add_quality_for_attribute(attribute=Attribute.MOLD, quality=get_quality_for_attr(quality_series, Attribute.MOLD))

        if Attribute.DAYLIGHT_FACTOR in measurements_df.columns:
            quality_series = measurements_df.apply(
                lambda row: (
                    Quality.EXCELLENT if row[Attribute.DAYLIGHT_FACTOR] >= 5 else
                    Quality.GOOD if (3.3 <= row[Attribute.DAYLIGHT_FACTOR] < 5) else
                    Quality.FAIR if (2.0 <= row[Attribute.DAYLIGHT_FACTOR] < 3.3) else
                    Quality.POOR
                ),
                axis=1
            )

            itr.add_quality_for_attribute(attribute=Attribute.DAYLIGHT_FACTOR, quality=get_quality_for_attr(quality_series, Attribute.DAYLIGHT_FACTOR))

        # Get the 95th percentile of the CO2 values
        if Attribute.CO2 in measurements_df.columns:
            co2_df = measurements_df[Attribute.CO2].copy() # pd.Series
            co2_df = co2_df.dropna()
            # Replace values below const.OUTDOOR_CO2 with outdoor CO2 value
            co2_df[co2_df < const.OUTDOOR_CO2] = const.OUTDOOR_CO2
            # Get the 95th percentile of the CO2 values
            co2_95 = co2_df.quantile(0.95)
            
            # Categorise the CO2 values
            quality = np.select(
                [co2_95 < 800,
                (800 <= co2_95 <= 1000),
                (1000 < co2_95 <= 1200),
                co2_95 > 1200],
                [Quality.EXCELLENT, Quality.GOOD, Quality.FAIR, Quality.POOR],
                default=np.nan
            ).item()
            # Set the category to the itr
            itr.add_quality_for_attribute(attribute=Attribute.CO2, quality=quality)

        if Attribute.SOUND_PRESSURE_LEVEL in measurements_df.columns:
            spl_df = measurements_df[Attribute.SOUND_PRESSURE_LEVEL].copy()
            spl_df = spl_df.dropna()
            # Replace values below const.MIN_SPL with const.MIN_SPL
            spl_df[spl_df < const.MIN_SPL] = const.MIN_SPL
            # Get the 5th percentile of the SPL values
            spl_5 = spl_df.quantile(0.05)

            # Categorise the SPL values depending on the room type (SMALL_OFFICE, OPEN_PLAN, HOTEL_ROOM)
            IMPLEMENTED_ROOM_TYPES = const.NOISE_CATEGORIES.keys()
            for room in rooms:
                if room.roomType in IMPLEMENTED_ROOM_TYPES:
                    categories = const.NOISE_CATEGORIES[room.roomType]
                    quality = np.select(
                        [spl_5 < categories[Quality.EXCELLENT],
                        (categories[Quality.EXCELLENT] <= spl_5 < categories[Quality.GOOD]),
                        (categories[Quality.GOOD] <= spl_5 <= categories[Quality.FAIR]),
                        spl_5 > categories[Quality.FAIR]],
                        [Quality.EXCELLENT, Quality.GOOD, Quality.FAIR, Quality.POOR],
                        default=np.nan
                    ).item()
                    room.add_quality_for_attribute(attribute=Attribute.SOUND_PRESSURE_LEVEL, quality=quality)
                
                elif room.roomType not in IMPLEMENTED_ROOM_TYPES:
                    # Warn that the room type is not implemented
                    print(f"Room type {room.roomType} is not implemented for noise categorisation")

        if Attribute.ILLUMINANCE in measurements_df.columns:
            ill_df = measurements_df[Attribute.ILLUMINANCE].copy()
            ill_df = ill_df.dropna()
            # Replace values below const.MIN_ILLUMINANCE with const.MIN_ILLUMINANCE
            ill_df[ill_df < const.MIN_ILLUMINANCE] = const.MIN_ILLUMINANCE

            if building.buildingType == BuildingType.OFFICE:
                percentage = ill_df.between(300, 500).sum() / len(ill_df)
                quality = np.select(
                    [percentage > 0.6,
                        (0.4 <= percentage <= 0.6),
                        (0.1 <= percentage < 0.4),
                        percentage < 0.1],
                    [Quality.EXCELLENT, Quality.GOOD, Quality.FAIR, Quality.POOR],
                    default=np.nan
                ).item()
                itr.add_quality_for_attribute(attribute=Attribute.ILLUMINANCE, quality=quality)

            elif building.buildingType == BuildingType.HOTEL:
                percentage = (ill_df >= 100).sum() / len(ill_df)

                quality = np.select(
                    [percentage == 0,
                        (0 < percentage <= 0.5),
                        (0.5 < percentage <= 0.9),
                        percentage > 0.9],
                    [Quality.EXCELLENT, Quality.GOOD, Quality.FAIR, Quality.POOR],
                    default=np.nan
                ).item()
                itr.add_quality_for_attribute(attribute=Attribute.ILLUMINANCE, quality=quality)

            else:
                # Warn that the building type is not implemented
                print(f"Building type {building.buildingType} is not implemented for illuminance categorisation")

    if agg_level == 'sensor':
        # We will need to take the least performing quality for each sensor and attribute and set it to the room quality
        for room in building.rooms:
            quality_dict = {}
            for sensor in room.sensors:
                for attribute, quality in sensor.quality.items():
                    if attribute not in quality_dict:
                        quality_dict[attribute] = []
                    quality_dict[attribute].append(quality)
            
            for attribute, qualities in quality_dict.items():
                rat = min(qualities)
                room.add_quality_for_attribute(attribute=attribute, quality=rat)

    return building

