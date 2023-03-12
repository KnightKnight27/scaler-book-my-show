from django.db import models
from .BaseModel import BaseModel
from .Show import Show
from .TicketStatus import TicketStatus
from .User import User
from .ShowSeat import ShowSeat


class Ticket(BaseModel):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE)
    show = models.ForeignKey(Show,on_delete=models.CASCADE)
    total_amount = models.FloatField()
    ticket_status = models.CharField(max_length=100, choices=[(ticket_status.name, ticket_status.value) for ticket_status in TicketStatus],
                                blank=True)
    time_of_booking = models.DateTimeField()
    show_seats = models.ManyToManyField(ShowSeat)
