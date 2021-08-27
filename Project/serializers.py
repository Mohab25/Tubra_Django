from .models import Project
from rest_framework.serializers import *


class ProjectListSerializer(HyperlinkedModelSerializer):
    projects = HyperlinkedRelatedField(read_only=True,view_name='project-list')
    class Meta:
        model = Project
        fields= '__all__'

class ProjectDetailsSerializer(HyperlinkedModelSerializer):
    id = ReadOnlyField()
    class Meta:
        model = Project
        fields='__all__'
