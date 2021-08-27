from django.db import models
from Aerodrome_features.models import Aerodrome_Entity , Aerodrome_Part
from Employee.models import Employee
from Aerodrome.models import Aerodrome

class DrawingSeries(models.Model):
    name = models.CharField(max_length=100)
    Aerodrome= models.ForeignKey(Aerodrome, related_name='CAD_Series', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering=['name']
    def __str__(self)->str:
        return self.name 

class Drawing(models.Model):
    Title = models.CharField(max_length=700)
    CAD_file = models.ImageField(null=True,max_length=700, blank=True, upload_to='../media/CAD/')
    Number_of_issuance = models.IntegerField(null=True, blank=True)
    Drawing_series = models.ForeignKey(DrawingSeries,related_name='drawing_series',null=True, blank=True, on_delete=models.SET_NULL)
    aerodrome_part = models.ForeignKey(Aerodrome_Part,related_name='CAD_Drawing', null=True, blank=True, on_delete=models.SET_NULL)
    Drawing_category = models.CharField(max_length=300, null=True,blank=True,default='')
    Aerodrome_Entity = models.ForeignKey(Aerodrome_Entity,related_name='CAD_Drawing',null=True, blank=True, on_delete = models.SET_NULL)
    Author = models.ForeignKey(Employee,related_name='CAD_Drawing',null=True, blank=True, on_delete = models.SET_NULL)
    #Department this is a many to many relation defined in the department model.
    Date_of_Authorization = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering=['Date_of_Authorization']
    def __str__(self)->str:
        return self.Title
