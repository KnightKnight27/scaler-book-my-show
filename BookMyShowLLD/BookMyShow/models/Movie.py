from django.db import models
from .BaseModel import BaseModel
from .Genre import Genre
from .Feature import Feature
from .Actor import Actor


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=100, choices=[(genre.name, genre.value) for genre in Genre],
                                blank=True)
    features = models.CharField(max_length=100, choices=[(feature.name, feature.value) for feature in Feature],
                                blank=True)
    actors = models.ManyToManyField(Actor)