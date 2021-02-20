from rest_framework import serializers 
from .models import *

class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(read_only=True)
    class Meta:
        model = DocumentType
        fields=('pk','url','type','documents')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields=('pk','url','name','document_type','document_file')