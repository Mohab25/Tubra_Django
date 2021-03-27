from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .linear_measure import make_linear_measure
from .buffer import make_buffer

@api_view(['GET','POST'])
def make_linear_measure_view(req):
    print('the request:',req.data)
    coords1 = req.data['coord1']
    coords2 = req.data['coord2']
    checker = True
    for i in coords1:
        print('type',type(i))
        if not isinstance(i,(float,int)):
            checker=False
    for i in coords2:
        if not isinstance(i,(float,int)):
            checker=False
    if not checker:
        return HttpResponse('not valid data')
    else:
        distance = make_linear_measure(coords1,coords2)
        print('distane:',distance)
        return HttpResponse(distance)



@api_view(['GET','POST'])
def make_buffer_view(req):
    geom = req.data['geom']
    radius = req.data['radius']
    checker = True
    # validate the geometry here 
    print('the request:',geom)

    if not isinstance(radius,(float,int)):
            checker=False
    if not checker:
        return HttpResponse('not valid data')
    else:
        print('the_geom',geom)
        buffer_geojson = make_buffer(geom,radius)
        return HttpResponse(buffer_geojson)