from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    modelo = models.IntegerField()