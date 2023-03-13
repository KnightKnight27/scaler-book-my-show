from enum import Enum


class ShowSeatStatus(Enum):
    BOOKED = "BOOKED"
    LOCKED = "LOCKED"
    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVIALABLE"