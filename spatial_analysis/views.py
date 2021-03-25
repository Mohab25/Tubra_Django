from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .linear_measure import make_linear_measure

@api_view(['GET','POST'])
@csrf_exempt
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