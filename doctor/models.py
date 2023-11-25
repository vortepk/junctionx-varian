from django.db import models


class Calendar(models.Model):
    machine_name = models.CharField(max_length=1024)
    slots = models.DateTimeField()


class Patient(models.Model):
    name = models.CharField(max_length=1024)
    family = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    weight = models.IntegerField()
    fractions_number = models.IntegerField()
    gender = models.CharField(max_length=1024)
    condition = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    treat_date = models.ManyToManyField(Calendar)


class Machine(models.Model):
    name = models.CharField(max_length=1024)
    family = models.CharField(max_length=1024)
