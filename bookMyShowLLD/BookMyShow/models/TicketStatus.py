from enum import Enum


class TicketStatus(Enum):
    CANCELLED = "CANCELLED"
    BOOKED = "BOOKED"
    PAYMENT_PENDING = "PAYMENT_PENDING"