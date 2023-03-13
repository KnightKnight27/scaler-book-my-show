from django.db import models
from .BaseModel import BaseModel
from .Movie import Movie

# THE RELATIONSHIP BETWEEN ACTOR AND MOVIE IS A MANY TO MANY RELATIONSHIP


class Actor(BaseModel):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)