from django.urls import path,re_path
from . import views 
urlpatterns=[
    path('linear_measure/',views.make_linear_measure_view,name='make-linear-measurement'),
]