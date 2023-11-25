from django.db import models


class Calendar(models.Model):
    machine_name = models.CharField(max_length=1024)
    slots = models.DateTimeField()


class Patient(models.Model):
    name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    sex = models.CharField(max_length=1024)
    weight = models.IntegerField()
    condition = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    fractions_number = models.IntegerField()
    treatment_date = models.ManyToManyField(Calendar)


class Machine(models.Model):
    name = models.CharField(max_length=1024)
    family = models.CharField(max_length=1024)


class Floor(models.Model):
    name = models.CharField(max_length=1024)
    wheelchair_accessible = models.BooleanField()
    has_elevator = models.BooleanField(default=False)


class Room(models.Model):
    number = models.CharField(max_length=1024)
    sex = models.CharField(max_length=1024)
    wheelchair_accessible = models.BooleanField()
    has_bath = models.BooleanField(default=True)
    area = models.IntegerField()  # Remoteness from treatment room zone


class Bed(models.Model):
    # Are there any specific beds?
    pass
