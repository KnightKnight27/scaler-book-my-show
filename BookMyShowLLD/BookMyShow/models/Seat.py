from django.db import models
from .BaseModel import BaseModel
from .SeatStatus import SeatStatus
from .Auditorium import Auditorium


class Seat(BaseModel):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    column = models.IntegerField()
    seat_status = models.CharField(max_length=100, choices=[(seat_status.name, seat_status.value) for seat_status in SeatStatus],
                                blank=True)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)