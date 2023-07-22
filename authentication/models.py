from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    point = models.IntegerField(default=0)
    contact = models.CharField(default=False, null=True, max_length=13)

class Point():
    point_amount = models.FloatField(default=False)
    date = models.DateField(default=False)