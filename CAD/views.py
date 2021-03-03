# look at the document views to see similar comments. 
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Drawing,DrawingSeries
from .serializers import DrawingsSerializer
import json
from django.http import HttpResponse

class DrawingList(ListCreateAPIView):
    queryset = Drawing.objects.all() 
    serializer_class = DrawingsSerializer
    name = 'drawing-list'

class DrawingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingsSerializer
    name = 'drawing-detail'

def cad_media_url_fix(request,pk):
        CAD = Drawing.objects.get(pk=pk)
        url = str(CAD.CAD_file).replace('/home/mohab/Main Folder/Master degree/Research/Tubra/venv+django/testenv/Tubra/media','media')
        print(url)
        url = 'http://localhost:8000/'+url
        content = json.dumps({'Title':CAD.Title,'url':url})
        return HttpResponse(content)


class DrawingSeriesList(ListCreateAPIView):
    queryset = DrawingSeries.objects.all() 
    serializer_class = DrawingsSerializer
    name = 'drawing_series-list'

class DrawingSeriesDetail(RetrieveUpdateDestroyAPIView):
    queryset = DrawingSeries.objects.all()
    serializer_class = DrawingsSerializer
    name = 'drawing_series-detail'
