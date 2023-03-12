from django.db import models
from .BaseModel import BaseModel
from .Feature import Feature
from .Theatre import Theatre


class Auditorium(BaseModel):
    name = models.CharField(max_length=255)
    features = models.CharField(max_length=100, choices=[(feature.name, feature.value) for feature in Feature], blank=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)