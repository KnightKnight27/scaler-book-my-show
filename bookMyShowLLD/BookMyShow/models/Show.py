from django.db import models
from .BaseModel import BaseModel
from .Auditorium import Auditorium
from .Movie import Movie
from .Feature import Feature

# TWO MODELS CAN HAVE MANY TO MANY RELATIONSHIP
# SO TO WRITE DOWN FEATURES AS A MANY TO MANY RELATION
# MAKE A MODEL FOR FEATURE TYPE
# class ShowFeature(BaseModel):
#     show_feature = models.CharField(choices = [])


class Show(BaseModel):
    show_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    show_auditorium = models.ForeignKey(Auditorium,on_delete=models.CASCADE)
    show_features = models.CharField(max_length=100, choices=[(feature.name, feature.value) for feature in Feature],
                                     blank=True)
    # show_features = models.ManyToManyField(ShowFeature)