from django.urls import path,re_path
from . import views 
urlpatterns=[
    path('linear_measure/',views.make_linear_measure_view,name='make-linear-measurement'),
    path('make_buffer/',views.make_buffer_view,name='make-buffer'),
    path('buffer_search/',views.buffer_search,name='buffer-search'),
]