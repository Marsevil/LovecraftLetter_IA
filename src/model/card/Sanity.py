from enum import Enum, unique

@unique
class Sanity(Enum):
    SANE = 1
    INSANE = 2
    NEUTRAL = 0
