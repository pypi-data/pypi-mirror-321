from .model import BuildingType, Quality, Room, PollutionLevel, RoomType

Q_p = {
    Quality.EXCELLENT: 10,
    Quality.GOOD: 7,
    Quality.FAIR: 4,
    Quality.POOR: 2.5
}

Q_B = {
    PollutionLevel.VERY_LOW_EMISSION: {
        Quality.EXCELLENT: 0.5,
        Quality.GOOD: 0.35,
        Quality.FAIR: 0.2,
        Quality.POOR: 0.15
    },
    PollutionLevel.LOW_EMISSION: {
        Quality.EXCELLENT: 1.0,
        Quality.GOOD: 0.7,
        Quality.FAIR: 0.4,
        Quality.POOR: 0.3
    },
    PollutionLevel.NON_LOW_EMISSION: {
        Quality.EXCELLENT: 2.0,
        Quality.GOOD: 1.4,
        Quality.FAIR: 0.8,
        Quality.POOR: 0.6
    },
}

def get_ventilation_rates(room: Room):
    pollution_level = room.pollutionLevel
    occupants = room.occupants
    floorArea = room.floorArea

    # Return a dictionary with the ventilation rates for each quality level calculated using the formula Q = Q_p * occupants + Q_B * floorArea

    return {
        quality: Q_p[quality] * occupants + Q_B[pollution_level][quality] * floorArea
        for quality in Quality
    }