from django.db import models

# Create your models here.

class Plant(models.Model):
    type = models.CharField(max_length=100)
<<<<<<< HEAD
    interval = models.Integerfield()
=======
    interval = models.IntegerField()
>>>>>>> 62d6d170541372ccf56ce8567b604ae377c967a8

class UserPlants(models.Model):
    name = models.CharField(max_length=100)
    nextWaterTime = models.TimeField()
    plantType = models.ForeignKey(Plant)