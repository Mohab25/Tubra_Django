from rest_framework import serializers 
from .models import *

class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document_Type
        fields=('pk','url','Doc_type')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    Document_type = DocumentTypeSerializer(read_only=True) # this will return the whole content above as an object.
    class Meta:
        model = Document
        fields=('pk','url','Name','Document_file','Aerodrome_Entity','Document_type')

class ObeidDocumentsSerializer(serializers.HyperlinkedModelSerializer):
    Document_type = DocumentTypeSerializer(read_only=True)
    class Meta:
        model = Document
        fields=('pk','url','Name','Document_file','Aerodrome_Entity','Document_type')
