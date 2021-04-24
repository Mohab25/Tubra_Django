from .models import City_Facility
from rest_framework import serializers

class City_Facility_Serializer(serializers.ModelSerializer):
    class Meta:
        model = City_Facility
        fields = '__all__'

