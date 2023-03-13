from enum import Enum


class PaymentType(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    UPI = "UPI"
    CASH = "CASH"
