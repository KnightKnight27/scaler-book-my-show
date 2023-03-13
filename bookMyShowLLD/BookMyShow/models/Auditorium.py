from .BaseModel import BaseModel
from django.db import models
from .Theatre import Theatre


class Auditorium(BaseModel):
    name = models.CharField(max_length=255)
    theatre_audi = models.ForeignKey(Theatre, on_delete=models.CASCADE,related_name='auditoriums' )
    # the relation between auditorium and feature is basically
    # many to many
    # features = models.ManyToManyField()