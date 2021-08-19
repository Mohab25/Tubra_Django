from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

class Facilities_List(ListCreateAPIView):
    queryset = City_Facility.objects.all()
    serializer_class = City_Facilities_List_Serializer
    name = 'city_facility-list'

class Facility_details(RetrieveUpdateDestroyAPIView):
    queryset = City_Facility.objects.all()
    serializer_class = City_Facilities_List_Serializer
    name = 'city_facility-detail'

class Blocks_List(ListCreateAPIView):
    queryset = City_Blocks.objects.all()
    serializer_class = City_Blocks_List_Serializer
    name = 'city_blocks-list'

class Blocks_details(RetrieveUpdateDestroyAPIView):
    queryset = City_Blocks.objects.all()
    serializer_class = City_Blocks_Details_Serializer
    name = 'city_blocks-detail'

class Streets_List(ListCreateAPIView):
    queryset = City_Streets.objects.all()
    serializer_class = City_Streets_List_Serializer
    name = 'city_streets-list'

class Streets_details(RetrieveUpdateDestroyAPIView):
    queryset = City_Streets.objects.all()
    serializer_class = City_Streets_Details_Serializer
    name = 'city_streets-detail'

class Districts_List(ListCreateAPIView):
    queryset = City_Districts.objects.all()
    serializer_class = City_Districts_List_Serializer 
    name = 'city_districts-list'

class Districts_details(RetrieveUpdateDestroyAPIView):
    queryset = City_Districts.objects.all()
    serializer_class = City_Districts_Details_Serializer
    name = 'city_districts-detail'

class Obeid_districts(ListCreateAPIView):
    queryset = Obeid_districts.objects.all()
    serializer_class = Obeid_districts_Serializer
    name = 'Obeid_districts'

class Obeid_streets(ListCreateAPIView):
    queryset = Obeid_streets.objects.all()
    serializer_class = Obeid_streets_Serializer
    name = 'Obeid_streets'

class Obeid_urban_areas(ListCreateAPIView):
    queryset = Ob_urban_area.objects.all()
    serializer_class = Obeid_urban_areas_Serializer
    name = 'Obeid_urban_areas'