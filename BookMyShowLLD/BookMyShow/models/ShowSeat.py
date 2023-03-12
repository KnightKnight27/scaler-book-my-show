from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .Seat import Seat
from .ShowSeatState import ShowSeatStatus


class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
  #  show_seat_state = EnumField(ShowSeatStatus)