from rest_framework import serializers 
from .models import * 
from Aerodrome_features.serializers import Aerodrome_Part_Serializer

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
    aerodrome_part = Aerodrome_Part_Serializer(read_only=True)
    class Meta:
        model = Drawing 
        fields='__all__'
