from django.db import models
from Aerodrome.models import Aerodrome

class Project(models.Model):
    Project_Name = models.CharField(max_length=300)
    Aerodrome= models.ForeignKey(Aerodrome, related_name='Project', null=True, on_delete=models.SET_NULL)

    # here there is a derived field of completion rate calculated from the number of 
    # phases completed over the total number of phases.
    def __str__(self):
        return self.Project_Name
    
class Phase(models.Model):
    Project = models.ForeignKey(Project,null=True,on_delete=models.SET_NULL) 
    Phase_Name = models.CharField(max_length=300)
    # here there is a derived field of completion rate calculated from the number of 
    # activities completed over the total number of activities.

    def __str__(self):
        return self.Phase_Name
    
class Activity(models.Model):
    Phase = models.ForeignKey(Phase,null=True,on_delete=models.SET_NULL)
    Activity_Name = models.CharField(max_length=300)
    Completion = models.BooleanField()

    def __str__(self):
        return self.Activity_Name

