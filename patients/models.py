from django.db import models

# Create your models here.

class Village(models.Model):
  name = models.CharField(max_length=200)

class Patient(models.Model):
    f_name = models.CharField(max_length=32)
    l_name = models.CharField(max_length=32)
    # village = relationshipToModel


class Doctor(models.Model):
    f_name = models.CharField(max_length=32)
    l_name = models.CharField(max_length=32)
    specialty = models.CharField(max_length=100)
