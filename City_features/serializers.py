from rest_framework.serializers import *
from .models import City_Blocks, City_Facility, City_Streets, City_Districts

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


class City_Blocks_List_Serializer(HyperlinkedModelSerializer):
    city_blocks = HyperlinkedRelatedField(read_only=True,view_name='city_blocks-list')
    class Meta:
        model = City_Blocks
        fields='__all__'

class City_Blocks_Details_Serializer(HyperlinkedModelSerializer):
    id = ReadOnlyField()
    class Meta: 
        model=City_Blocks
        fields = '__all__'


class City_Streets_List_Serializer(HyperlinkedModelSerializer):
    city_blocks = HyperlinkedRelatedField(read_only=True,view_name='city_streets-list')
    class Meta:
        model = City_Streets
        fields='__all__'

class City_Streets_Details_Serializer(HyperlinkedModelSerializer):
    id = ReadOnlyField()
    class Meta: 
        model=City_Streets
        fields = '__all__'

class City_Districts_List_Serializer(HyperlinkedModelSerializer):
    city_blocks = HyperlinkedRelatedField(read_only=True,view_name='city_districts-list')
    class Meta:
        model = City_Districts
        fields='__all__'

class City_Districts_Details_Serializer(HyperlinkedModelSerializer):
    id = ReadOnlyField()
    class Meta: 
        model=City_Districts
        fields = '__all__'
