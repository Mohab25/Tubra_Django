from rest_framework.serializers import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

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

class Obeid_districts_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Obeid_districts
        geo_field='geom'
        fields='__all__' 

class Obeid_streets_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Obeid_streets
        geo_field='geom'
        fields='__all__' 

class Obeid_urban_areas_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ob_urban_area
        geo_field='geom'
        fields='__all__' 