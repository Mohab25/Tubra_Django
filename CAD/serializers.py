from rest_framework import serializers 
from .models import * 

class DrawingSeriesSerializer(serializers.HyperlinkedModelSerializer):
    drawings = serializers.HyperLinkedRelatedField(read_only=True)
    class Meta:
        model = DrawingSeries
        fields=('pk','url','name','drawings')

class DrawingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drawing 
        fields=('pk', 'url', 'name', 'tile_file', 'drawing_series')

