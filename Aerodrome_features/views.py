from django.shortcuts import render 
from .models import *
from .serializers import *
from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.Response import Response
# @api_view(['GET','POST'])
# def Aerodrome_Features_list(request):
#     if request.method =='GET':
#         # grab the data from the database, serialize it and send it
#         Features = Aerodrome_Entity.objects.all()
#         Serialized_Features = FeaturesSerializer(Features,many=True)
#         return Response(Serialized_Features.data,status=status.HTTP_200_SUCCESS)
#     if request.method == 'POST':
#         serialized_data = FeaturesSerializer(data = request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response(serialized_data,status=status.HTTP_201_Created)
#         else:
#             return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

class AerodromeFeaturesListView(generics.ListCreateAPIView):
    queryset = Aerodrome_Entity.objects.all()
    serializer_class = FeatureSerializer
    name = 'Aerodrome_Features_List_View'

class AerodromeFeaturesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aerodrome_Entity.objects.all()
    serializer_class = FeatureSerializer
    name = 'aerodrome_entity-detail'

class AerodromeFeaturesPavementConstructions(generics.ListCreateAPIView):
    queryset = Pavement_Construction.objects.all()
    serializer_class = Pavement_Construction_Serializer
    name = 'pavement_constructions'


class AerodromeFeaturesPavementConstructionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pavement_Construction.objects.all()
    serializer_class = Pavement_Construction_Serializer
    name = 'pavement_construction-details'

class AerodromeFeaturesPOI(generics.ListCreateAPIView):
    queryset = Aerodrome_Entity.objects.filter(Aerodrome=1).exclude(Category='Aerodrome Builds')
    serializer_class = FeatureSerializer
    name = 'aerodrome_entity_poi-list'

class Aerodrome_Entity_Image_Detail_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aerodrome_Entity.objects.all()
    serializer_class = Aerodrome_Entity_Image_Serializer
    name = 'Aerodrome_Entity_Detail_View'

class Aerodrome_Entity_Image_List_View(generics.ListCreateAPIView):
    queryset = Aerodrome_Entity.objects.all()
    serializer_class = Aerodrome_Entity_Image_Serializer
    name = 'Aerodrome_Entity_Image_List_View'

class Aerodrome_Entity_Image_Detail_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aerodrome_Entity.objects.all()
    serializer_class = Aerodrome_Entity_Image_Serializer
    name = 'Aerodrome_Entity_Image_Detail_View'

