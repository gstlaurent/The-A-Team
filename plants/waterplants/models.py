from django.db import models

# Create your models here.

class Plant(models.Model):
    type = models.CharField(max_length=100)
    interval = models.TimeField()

class UserPlants(models.Model):
    name = models.CharField(max_length=100)
    plantType = models.ForeignKey(Plant)
    nextWaterTime = models.TimeField()