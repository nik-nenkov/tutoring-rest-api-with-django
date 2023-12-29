from django.db import models
from django.db.models.manager import Manager


class Actor(models.Model):
    objects: Manager = models.Manager()
    name = models.CharField(max_length=100)


class Transporter(models.Model):
    objects: Manager = models.Manager()
    license_plate = models.CharField(max_length=20)


class Load(models.Model):
    objects: Manager = models.Manager()
    weight = models.FloatField()
    description = models.TextField()


class Storage(models.Model):
    objects: Manager = models.Manager()
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
