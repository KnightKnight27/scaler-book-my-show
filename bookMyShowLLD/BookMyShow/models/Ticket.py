from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .User import User
from .TicketStatus import TicketStatus
from .ShowSeat import ShowSeat


class Ticket(BaseModel):
    ticket_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    total_amount = models.FloatField()
    ticket_status = models.CharField(max_length=255,
                                     choices=[(status.name,status.value) for status in TicketStatus])
    # many to many relation ship
    # reason is -> cancelled tickets (hint)
    show_seats = models.ManyToManyField(ShowSeat)