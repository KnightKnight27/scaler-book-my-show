from django.db import models
from .BaseModel import BaseModel
from .PaymentType import PaymentType
from .PaymentStatus import PaymentStatus
from .Ticket import Ticket


class Payment(BaseModel):
    payment_type = models.CharField(max_length=255,
                                    choices = [(p.name,p.value) for p in PaymentType])
    payment_status = models.CharField(max_length=255,
                                      choices = [(p.name,p.value) for p in PaymentStatus])
    payment_ticket = models.ForeignKey(Ticket,on_delete=models.DO_NOTHING)
    payment_time = models.DateTimeField()
    reference_id = models.CharField(max_length=255)
    # bcz payments are handled by third party applications in most cases
    amount = models.FloatField()
