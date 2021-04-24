from django.db import models
from Aerodrome_features.models import Aerodrome_Entity 
from Aerodrome.models import Aerodrome

class Document_Type(models.Model):
    Doc_type = models.CharField(max_length=50)
    def __str__(self)->str:
        return self.Doc_type


class Document(models.Model):
    Name = models.CharField(max_length=300)
    Document_type = models.ForeignKey(Document_Type,null=True,on_delete=models.SET_NULL)
    Document_file = models.FileField(max_length=500)
    Aerodrome_Entity = models.ForeignKey(Aerodrome_Entity,related_name='Reports',null=True,on_delete=models.SET_NULL)
    Aerodrome= models.ForeignKey(Aerodrome, related_name='Reports', null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=['id']
    def __str__(self)->str:
        return self.Name
