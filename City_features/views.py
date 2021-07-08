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
    name = 'city_facility-list'