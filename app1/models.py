from django.db import models

# Create your models here.

class Employee(models.Model):
  nombre: models.CharField = models.CharField(max_length=50)
  email : models.CharField = models.CharField(max_length=50)
  fono  : models.CharField= models.CharField(max_length=15)