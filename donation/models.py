from django.db import models

class Donation(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField()
    datetime_created = models.DateTimeField()
    weight_grams = models.PositiveIntegerField()
    address = models.TextField()
    description = models.TextField(blank=True)