from django.db import models
from .BaseModel import BaseModel
from .SeatStatus import SeatStatus
from .Auditorium import Auditorium


class Seat(BaseModel):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    column = models.IntegerField()
    seat_auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    seat_status = models.CharField(max_length=255,
            choices=[(status.name, status.value) for status in SeatStatus])