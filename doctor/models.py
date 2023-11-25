from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)
    sex = models.CharField(max_length=1024, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    fractions_number = models.IntegerField(blank=True, null=True)
    priority = models.BooleanField(max_length=1024, blank=True, null=True)
    large_bodied = models.BooleanField(default=False)
    breath_holding = models.BooleanField(default=False)
    inpatient = models.BooleanField(default=False)


class Machine(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    in_service = models.BooleanField(default=True)


class Timeslot(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    machine = models.ForeignKey(Machine, on_delete=models.DO_NOTHING)


class Floor(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    wheelchair_accessible = models.BooleanField(default=True)
    has_elevator = models.BooleanField(default=True)


class Room(models.Model):
    number = models.CharField(max_length=1024, blank=True, null=True)
    sex = models.CharField(max_length=1024, blank=True, null=True)
    wheelchair_accessible = models.BooleanField(default=True)
    has_bath = models.BooleanField(default=True)
    area = models.IntegerField(blank=True, null=True)  # Remoteness from treatment room zone


class Bed(models.Model):
    # Are there any specific beds?
    pass
