from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .SeatType import SeatType


class ShowSeatType(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.FloatField()
    seat_type = models.CharField(max_length=10, choices=[(c.name, c.value) for c in SeatType])