# look at the document views to see similar comments. 
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Drawing,DrawingSeries
from .serializers import DrawingsListSerializer, DrawingsDetailsSerializer, DrawingSeriesSerializer
import json
from django.http import HttpResponse

class DrawingList(ListCreateAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingsListSerializer
    name = 'drawing-list'

class DrawingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingsDetailsSerializer
    name = 'drawing-detail'

class DrawingSeriesList(ListCreateAPIView):
    queryset = DrawingSeries.objects.all()
    serializer_class = DrawingSeriesSerializer
    name = 'drawing_series-list'

class DrawingSeriesDetail(RetrieveUpdateDestroyAPIView):
    queryset = DrawingSeries.objects.all()
    serializer_class = DrawingSeriesSerializer
    name = 'drawingseries-detail'
