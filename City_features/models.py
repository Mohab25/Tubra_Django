from django.contrib.gis.db import models
from Aerodrome.models import Aerodrome

class City_Facility(models.Model):
    City_Name = models.CharField(max_length=100)
    Facility_Name = models.CharField(max_length=200)
    Description = models.TextField(null=True)
    Elevation = models.FloatField(null=True)
    Category = models.CharField(max_length=100,null=True)
    Aerodrome= models.ForeignKey(Aerodrome, related_name='City', null=True, on_delete=models.SET_NULL)
    geom = models.GeometryField(null=True)

    class Meta:
        ordering=['pk']
    
    def __str__(self):
        return self.Facility_Name

class City_Blocks(models.Model):
    City_Name = models.CharField(max_length=100)
    Block_Name = models.CharField(max_length=300)
    Block_Arabic_Name = models.CharField(max_length=300)
    Block_Number = models.CharField(max_length=300,null=True)
    Block_Class = models.CharField(max_length=100,null=True)
    geom = models.MultiPolygonField(null=True)
    class Meta:
        ordering=['id']


class City_Streets(models.Model):
    City_Name = models.CharField(max_length=100)
    Street_Name = models.CharField(max_length=100)
    Street_Name_Arabic = models.CharField(max_length=100)
    Street_Class = models.CharField(max_length=100)
    Street_Class_Arabic = models.CharField(max_length=100)
    geom = models.MultiLineStringField(null=True)
    class Meta:
        ordering=['id']

class City_Districts(models.Model):
    City_Name = models.CharField(max_length=100)
    District_Name = models.CharField(max_length=100)
    District_Name_Arabic = models.CharField(max_length=100)
    District_Code = models.CharField(null=True,max_length=1)
    geom = models.MultiPolygonField(null=True)
    class Meta:
        ordering=['id']