from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    point = models.FloatField(default=False)

class Point():
    point_amount = models.FloatField(default=False)
    date = models.DateField(default=False)