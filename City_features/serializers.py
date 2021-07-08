from rest_framework.serializers import *
from .models import City_Facility

class City_Facilities_List_Serializer(HyperlinkedModelSerializer):
    city_facilities = HyperlinkedRelatedField(read_only=True,view_name='city_facility-list')
    class Meta:
        model = City_Facility
        fields = '__all__'

class City_Facility_Details_Serializer(HyperlinkedModelSerializer):
    id = ReadOnlyField()
    class Meta:
        model = City_Facility
        fields = '__all__'