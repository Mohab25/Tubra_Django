from django.http.response import HttpResponse
from django.shortcuts import render 
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from django.apps import apps
import re
import json

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
    queryset = Pavement.objects.all()
    serializer_class = Pavement_Serializer
    name = 'Pavements'


class AerodromeFeaturesPavementConstructionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pavement.objects.all()
    serializer_class = Pavement_Serializer
    name = 'Pavement-details'

# class AerodromeFeaturesPOI(generics.ListCreateAPIView):
#     queryset = Aerodrome_Entity.objects.filter(Aerodrome=1).exclude(Aerodrome_Part='Aerodrome Builds')
#     serializer_class = FeatureSerializer
#     name = 'aerodrome_entity_poi-list'

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

@api_view(['POST'])
def add_aerodrome_features(req):
    # getting the data from the req, serialize it, check if valid and save to the model 
    data = req.data
    print('The post data',data)
    serialized_data = FeatureSerializer(data=data)
    if serialized_data.is_valid():
        serialized_data.save()
        return HttpResponse(serialized_data.data,status.HTTP_201_CREATED)
    else:
        return HttpResponse(serialized_data.errors,status.HTTP_400_BAD_REQUEST)


def get_fields_name_for_forms(req,modelName):
    model = apps.get_model('Aerodrome_features', modelName)
    fieldsNames = model._meta.get_fields()
    names=[]
    for i in fieldsNames:
        i = str(i)
        for l in ['Aerodrome_features.Aerodrome_Entity.','>','<','ManyToOneRel','ManyToManyRel','Aerodrome_features.',':','aerodromeutility']:
            if i.find(l)+1:
                i= i.replace(l,'')
            else:
                continue
        names.append(re.sub(r'\s+','',i))
    names=json.dumps({'form_titles':names})
    return HttpResponse(names)


class Obeid_Aerodrome_Parts(generics.ListCreateAPIView):
    queryset = airport_parts.objects.all()
    serializer_class = Obeid_Aerodrome_Parts_Serializer
    name = 'Obeid_Aerodrome_Parts'