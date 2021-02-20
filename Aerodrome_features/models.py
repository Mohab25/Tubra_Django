from django.contrib.gis.db import models
from Aerodrome.models import Aerodrome

class Aerodrome_Part(models.Model):
    Name = models.CharField(max_length=200)
    geom = models.PolygonField()
    # for str the model name will be returned, for ordering no particular order is required.

class Aerodrome_Entity(models.Model):
    Aerodrome= models.ForeignKey(Aerodrome, related_name='Aerodrome_Entity', null=True, on_delete=models.SET_NULL)
    Feature_Name = models.CharField(max_length=500)
    Aerodrome_Part_ID = models.ForeignKey(Aerodrome_Part,null=True,on_delete=models.SET_NULL)
    geom =  models.GeometryCollectionField() # this is tricky, i think i need inheritance here (point,line..)
    Entity_Condition = models.CharField(max_length=100)
    Survey_Date = models.DateTimeField()
    Description = models.TextField()

    class Meta:
        ordering=['Feature_Name']
    
    def __str__(self)->str:
        return self.Feature_Name


class Pavement_Construction(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Pavement_Name = models.CharField(max_length=100)
    Width = models.FloatField()
    Shoulder_Width = models.FloatField()
    Design_Types = [('f','Flexible Design'),('r','Rigid Pavement')]
    Pavement_Design_Type = models.CharField(max_length=1,choices=Design_Types)
    Subgrade_Density = models.FloatField()
    Subgrade_Soil_Classification = models.CharField(max_length=100)
    Soil_Shear_Strength = models.FloatField()
    Soil_DCP_Test_Result = models.FloatField()
    Soil_CPT_Test_Result = models.FloatField()
    Soil_Percolation_Rate = models.FloatField()
    SubBase_Material = models.CharField(max_length=100)
    SubBase_Thickness = models.FloatField()
    Joint_Spacing = models.FloatField()
    SubBase_Base_Seperation_Material = models.CharField(max_length=100)
    Base_Material = models.CharField(max_length=100)
    Base_Thickness = models.CharField(max_length=100)
    Concrete_Compressive_Strength = models.FloatField()
    Asphalt_Thickness = models.FloatField()
    Binder_Thickness = models.FloatField()
    Wearing_Thickness = models.FloatField()
    Drainage_Longitudinal_Slope = models.FloatField()
    Drainage_Cross_Slope = models.FloatField() 
    Pavement_geom = models.PolygonField() # set Aerodrome geom to null.

    class Meta:
        ordering=['Pavement_Name']
    

class Aerodrome_Utility_Pole(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Tension_Types = [('H','High Tension'),('L','Low Tension'),('B','High/Low Tension')]
    Tension_Type = models.CharField(max_length=1,choices=Tension_Types)
    Cable_Size = models.FloatField()
    Pole_Type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Remark = models.TextField()
    Pole_geom = models.PointField()

class Aerodrome_Utility_Electric_Cable(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Cable_Size= models.FloatField()
    Remark = models.TextField()
    Cable_geom = models.LineStringField()


class Aerodrome_Utility_Water_Line(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Line_Size= models.FloatField()
    Remark = models.TextField()
    Line_geom = models.LineStringField()

class Aerodrome_Utility_Gas_Line(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Line_Size= models.FloatField()
    Remark = models.TextField()
    Line_geom = models.LineStringField()

class Aerodrome_Utility_Sewage_Line(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Line_Size= models.FloatField()
    Remark = models.TextField()
    Line_geom = models.LineStringField()
  

class Aerodrome_Entity_Image(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField()
    Aerodrome_Entity = models.ForeignKey(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.Name