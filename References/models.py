from django.db import models
from Aerodrome_features.models import Aerodrome_Entity

class Reference(models.Model):
    Name = models.CharField(max_length=200)
    Reference_File = models.FileField()
    Aerodrome_Entity = models.ForeignKey(Aerodrome_Entity,null=True ,on_delete=models.SET_NULL)

    def __str__(self)->str:
        return self.Name
    
