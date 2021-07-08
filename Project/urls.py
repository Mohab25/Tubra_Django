from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('projects/',ProjectsList.as_view(),name='project-list'),
    re_path(r'project/(?P<pk>\d+)/$',ProjectDetails.as_view(),name='project-detail')
]