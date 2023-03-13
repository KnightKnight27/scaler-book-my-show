from enum import Enum


class PaymentStatus(Enum):
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    DONE = "DONE"