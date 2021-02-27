from rest_framework import serializers 
from .models import * 

class DrawingSeriesSerializer(serializers.HyperlinkedModelSerializer):
    drawings = serializers.HyperlinkedRelatedField(read_only=True,view_name='drawing-list')
    class Meta:
        model = DrawingSeries
        fields='__all__'

class DrawingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drawing 
        fields='__all__'

