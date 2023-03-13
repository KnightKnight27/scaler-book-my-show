from .BaseModel import BaseModel
from django.db import models
from .City import City


class Theatre(BaseModel):
    name = models.CharField(max_length=255)
    theatre_city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    # IT CAN HAVE A LIST OF AUDTIORIUMS