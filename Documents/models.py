from django.db import models
from Aerodrome_features.models import Aerodrome_Entity 
from Aerodrome.models import Aerodrome

class Document_Type(models.Model):
    Doc_type = models.CharField(max_length=50)

    # for str the model name will be returned, for ordering no particular order is required.


class Document(models.Model):
    Name = models.CharField(max_length=100)
    Document_type = models.ForeignKey(Document_Type,related_name='Reports',null=True,on_delete=models.SET_NULL)
    Document_file = models.FileField()
    Aerodrome_Entity = models.ForeignKey(Aerodrome_Entity,related_name='Reports',null=True,on_delete=models.SET_NULL)
    Aerodrome= models.ForeignKey(Aerodrome, related_name='Reports', null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering=['id']
    def __str__(self)->str:
        return self.name

