from django.db import models
from .BaseModel import BaseModel
from .Auditorium import Auditorium
from .Feature import Feature
from .Movie import Movie


class Show(BaseModel):
    start_time = models.TimeField()
    end_time = models.TimeField()
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_features = models.CharField(max_length=100, choices=[(feature.name, feature.value) for feature in Feature],
                                blank=True)