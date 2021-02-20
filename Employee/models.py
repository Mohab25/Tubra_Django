from django.db import models
from Aerodrome_features.models import Aerodrome_Entity
from Project.models import Project

class Employee(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=13)
    #Department = relation should be made in the Department class
    Role = models.CharField(max_length=100)
    Current_employment_status = models.CharField(max_length=100)
    Aerodrome_Entity = models.ManyToManyField(Aerodrome_Entity)
    Project = models.ManyToManyField(Project)

    class Meta:
        ordering = ['First_Name','Last_Name']
    
    def __str__(self):
        return self.first_name
