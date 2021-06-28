from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('',Employee_List.as_view(),name='employee-list'),
    re_path(r'employee/(?P<pk>\d+)/$',Employee_Details.as_view(), name='employee-detail'),
]