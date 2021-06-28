from rest_framework import serializers 
from .models import * 

class AerodromeListSerializer(serializers.HyperlinkedModelSerializer):
    aerodromes = serializers.HyperlinkedRelatedField(read_only=True,view_name='aerodrome-list')
    class Meta:
        model = Aerodrome
        fields='__all__'

class AerodromeDetailsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Aerodrome 
        fields='__all__'
