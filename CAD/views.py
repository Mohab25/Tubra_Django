# look at the document views to see similar comments. 
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Drawing
from .serializers import DrawingsSerializer

class DrawingList(ListCreateAPIView):
    queryset = Drawing.objects.all() 
    serializer_class = DrawingsSerializer
    name = 'drawing-list'

class DrawingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingsSerializer
    name = 'drawing-detail'
