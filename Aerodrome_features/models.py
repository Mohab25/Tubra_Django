from django.contrib.gis.db import models
from Aerodrome.models import Aerodrome

class Aerodrome_Part(models.Model):
    Name = models.CharField(max_length=200)
    geom = models.PolygonField()
    # for str the model name will be returned, for ordering no particular order is required.

class Aerodrome_Entity(models.Model):
    Aerodrome= models.ForeignKey(Aerodrome, related_name='Aerodrome_Entity', null=True, on_delete=models.SET_NULL)
    Feature_Name = models.CharField(max_length=500,null=True)
    Aerodrome_Part_ID = models.ForeignKey(Aerodrome_Part,null=True,on_delete=models.SET_NULL)
    Category = models.CharField(max_length=300,null=True)
    Elevation = models.FloatField(null=True)
    geom =  models.GeometryField(null=True)
    Entity_Condition = models.CharField(max_length=100,null=True)
    Survey_Date = models.DateField(null=True)
    Description = models.TextField(null=True)

    class Meta:
        ordering=['id']
    
    # def __str__(self)->str:
    #     str(self.id)


class Pavement_Construction(models.Model):
    Aerodrome_Entity = models.OneToOneField(Aerodrome_Entity,null=True,on_delete=models.SET_NULL)
    Pavement_Name = models.CharField(max_length=100)
    Width = models.FloatField(null=True)
    Shoulder_Width = models.FloatField(null=True)
    Design_Types = [('f','Flexible Design'),('r','Rigid Pavement')]
    Pavement_Design_Type = models.CharField(max_length=1,choices=Design_Types,null=True)
    Subgrade_Density = models.FloatField(null=True)
    Subgrade_Soil_Classification = models.CharField(max_length=100,null=True)
    Soil_Shear_Strength = models.FloatField(null=True)
    Soil_DCP_Test_Result = models.FloatField(null=True)
    Soil_CPT_Test_Result = models.FloatField(null=True)
    Soil_Percolation_Rate = models.FloatField(null=True)
    SubBase_Material = models.CharField(max_length=100,null=True)
    SubBase_Thickness = models.FloatField(null=True)
    Joint_Spacing = models.FloatField(null=True)
    SubBase_Base_Seperation_Material = models.CharField(max_length=100,null=True)
    Base_Material = models.CharField(max_length=100,null=True)
    Base_Thickness = models.CharField(max_length=100,null=True)
    Concrete_Compressive_Strength = models.FloatField(null=True)
    Asphalt_Thickness = models.FloatField(null=True)
    Binder_Thickness = models.FloatField(null=True)
    Wearing_Thickness = models.FloatField(null=True)
    Drainage_Longitudinal_Slope = models.FloatField(null=True)
    Drainage_Cross_Slope = models.FloatField(null=True) 
    Pavement_geom = models.MultiPolygonField() # set Aerodrome geom to null.

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