from django.db import models
from .BaseModel import BaseModel
from .Ticket import Ticket


class Payment(BaseModel):
    payment_time = models.DateTimeField()
    amount = models.FloatField()
    reference_id = models.CharField(max_length=255)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    # PAYMENT STATUS AND PAYMENT METHOD IS LEFT
    