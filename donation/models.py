from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Donation(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    datetime_created = models.DateTimeField()
    weight_grams = models.PositiveIntegerField()
    address = models.TextField()
    description = models.TextField(blank=True)