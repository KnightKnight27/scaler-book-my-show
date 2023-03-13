from django.db import models
from .BaseModel import BaseModel
from .Genre import Genre


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    actors = models.ManyToManyField(to='Actor')
    genre = models.CharField(max_length=255,choices = [(genre.name,genre.value) for genre in Genre])