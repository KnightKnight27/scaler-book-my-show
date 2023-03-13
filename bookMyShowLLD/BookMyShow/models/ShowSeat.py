from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .Seat import Seat
from .ShowSeatType import ShowSeatType
from .ShowSeatStatus import ShowSeatStatus


class ShowSeat(BaseModel):
    show_seat_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    show_seat_seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_seat_type = models.ForeignKey(ShowSeatType, on_delete=models.CASCADE)
    show_seat_status = models.CharField(max_length=255, choices=
                                [(status.name,status.value)for status in ShowSeatStatus]
                            )

    def get_all_seats_by_id(self,show_seat_ids):
        return ShowSeat.objects.select_for_update().filter(id__in=show_seat_ids)
    # if you are using select for update
    # the database rows get locked
    # any other user will not be able to access these seats till the time you have completed
    # your transaction