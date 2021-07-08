from django.shortcuts import render
from rest_framework.generics import *
from .models import * 
from .serializers import *


class ProjectsList(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    name = 'project-list'


class ProjectDetails(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailsSerializer
    name = 'project-detail'

