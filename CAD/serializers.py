from rest_framework import serializers 
from .models import * 

class DrawingSeriesSerializer(serializers.HyperlinkedModelSerializer):
    drawings = serializers.HyperlinkedRelatedField(read_only=True,view_name='drawing-list')
    id = serializers.ReadOnlyField()
    class Meta:
        model = DrawingSeries
        fields='__all__'

class DrawingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'

class DrawingsDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Drawing 
        fields='__all__'
