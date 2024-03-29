from rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class Aerodrome_Part_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aerodrome_Part
        fields = '__all__'

class FeatureSerializer(GeoFeatureModelSerializer):
    # Pavement_set = serializers.SlugRelatedField(slug_field='Pavement_Name',many=True, read_only=True)
    # Aerodrome_Utility_Pole_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True,allow_null=True)
    # Aerodrome_Utility_Electric_Cable_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True,allow_null=True)
    # Aerodrome_Utility_Water_Line_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True,allow_null=True)
    # Aerodrome_Utility_Gas_Line_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True,allow_null=True)
    # Aerodrome_Utility_Sewage_Line_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True,allow_null=True)
    # Aerodrome_Entity_Image_set = serializers.HyperlinkedRelatedField(read_only=True,many=True,allow_null=True,view_name='Aerodrome_Entity_Image_Detail_View')
    # Drawing_set = serializers.HyperlinkedRelatedField(read_only=True,many=True,allow_null=True,view_name='drawing-detail')
    Reports = serializers.HyperlinkedRelatedField(read_only=True,many=True,allow_null=True,view_name='document-detail')
    # Employee_set = serializers.StringRelatedField(read_only=True,many=True)
    #Reference_set = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='reference-detail')
   
    class Meta:
        model = Aerodrome_Entity 
        geo_field = 'geom'
        fields=['Aerodrome','Feature_Name','Aerodrome_Part_ID','Category','Elevation','geom','Entity_Condition','Survey_Date','Description','Pavement_set','aerodrome_utility_pole_set','aerodrome_utility_electric_cable_set','aerodrome_utility_water_line_set','aerodrome_utility_gas_line_set','aerodrome_utility_sewage_line_set','aerodrome_entity_image_set','Reports']

class Pavement_Serializer(GeoFeatureModelSerializer):
    #Aerodrome_Entity = serializers.SlugRelatedField(slug_field='Feature_Name',read_only=True) # this will be the same as StringRelatedField because the __str__ method of the Aerodrome_Entity returns the Feature_Name
    Aerodrome_Entity = FeatureSerializer()
    class Meta:
        model = Pavement
        geo_field = 'Pavement_geom'
        fields = '__all__'
    
# class Aerodrome_Utility_Pole_Serializer(serializers.ModelSerializer):
#     Aerodrome_Entity_Name = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Aerodrome_Utility_Pole
#         fields='__all__'

# class Aerodrome_Utility_Electric_Cable_Serializer(serializers.ModelSerializer):
#     Aerodrome_Entity_Name = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Aerodrome_Utility_Electric_Cable
#         fields='__all__'

# class Aerodrome_Utility_Water_Line_Serializer(serializers.ModelSerializer):
#     Aerodrome_Entity_Name = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Aerodrome_Utility_Water_Line
#         fields='__all__'

# class Aerodrome_Utility_Sewage_Line_Serializer(serializers.ModelSerializer):
#     Aerodrome_Entity_Name = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Aerodrome_Utility_Sewage_Line
#         fields='__all__'

class Aerodrome_Entity_Image_Serializer(serializers.ModelSerializer):
    Aerodrome_Entity_Name = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='Aerodrome_Entity_Detail_View')
    class Meta:
        model = Aerodrome_Entity_Image
        fields='__all__'

# class CAD_Drawings_Serializer(serializers.ModelSerializer):

class Obeid_Aerodrome_Parts_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = airport_parts
        geo_field='geom'
        fields='__all__'

class POIsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POIs
        geo_field = 'geom'
        fields = '__all__'