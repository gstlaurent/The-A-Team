from django.db import models

# Create your models here.

class Plant(models.Model):
    type = models.CharField(max_length=100)
    interval = models.IntegerField()

class UserPlants(models.Model):
    name = models.CharField(max_length=100)
    nextWaterTime = models.TimeField()
    plantType = models.ForeignKey(Plant)