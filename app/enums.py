from enum import IntEnum


class BaseEnum(IntEnum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def values(cls):
        return [key.value for key in cls]


class CarType(BaseEnum):
    SMALL_CAR = 1
    FAMILY_CAR = 2
    VAN = 3
