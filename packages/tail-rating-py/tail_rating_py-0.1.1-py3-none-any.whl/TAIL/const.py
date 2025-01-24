from .model import RoomType, Quality, BuildingType 

OUTDOOR_CO2 = 420 # ppm
MIN_SPL = 20 # dB(A) - Minimum sound pressure level based on the measurement device

NOISE_CATEGORIES = {
    RoomType.SMALL_OFFICE: {
        Quality.EXCELLENT: 30,
        Quality.GOOD: 35,
        Quality.FAIR: 40
    },
    RoomType.OPEN_PLAN_OFFICE: {
        Quality.EXCELLENT: 35,
        Quality.GOOD: 40,
        Quality.FAIR: 45
    },
    RoomType.HOTEL_ROOM: {
        Quality.EXCELLENT: 25,
        Quality.GOOD: 30,
        Quality.FAIR: 35
    }
}

MIN_ILLUMINANCE = 30 # lux
