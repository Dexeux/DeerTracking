from django.db import models
import time
import datetime

# Create your models here.
class migration_csv_import(models.Model):
    event_id = models.IntegerField()
    timestamp = models.CharField(max_length=50)
    location_long = models.FloatField()
    location_lat = models.FloatField()
    individual_local_identifier = models.IntegerField()
    study_name = models.CharField(max_length=200)

class Animal(models.Model):
    animal_name = models.CharField(max_length=200)
    tag_id = models.IntegerField(default=0)
    def __str__(self):
        return self.tag_id

class LocationPoint(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=50)
    location_long = models.IntegerField(default=0)
    location_lat = models.IntegerField(default=0)
    migration_stage = models.CharField(max_length=50)
    migration_status = models.CharField(max_length=50)
    def __str__(self):
        return location_long, location_lat