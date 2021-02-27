from rest_framework import serializers 
from .models import *

class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(read_only=True,view_name='document-list')
    class Meta:
        model = Document_Type
        fields=('pk','url','type','documents')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields=('pk','url','Name','Document_type','Document_file')