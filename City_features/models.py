from django.contrib.gis.db import models
from Aerodrome.models import Aerodrome

class City_Facility(models.Model):
    Facility_Name = models.CharField(max_length=200)
    Description = models.TextField()
    Height = models.FloatField()
    Aerodrome= models.ForeignKey(Aerodrome, related_name='City', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering=['pk']
    
    def __str__(self):
        return self.Facility_Name
