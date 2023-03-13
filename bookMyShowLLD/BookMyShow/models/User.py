from django.db import models
from .BaseModel import BaseModel


class User(BaseModel):
    email = models.EmailField()
    name = models.CharField(max_length=255)