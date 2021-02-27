from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('drawings/',DrawingList.as_view(),name='drawing-list'),
    path('drawing_series/',DrawingSeriesList.as_view(),name='drawing_series-list'),
    re_path(r'drawing/(?P<pk>\d+)/$',DrawingDetail.as_view(),name='drawing-detail'),
    re_path(r'drawing_series/(?P<pk>\d+)/$',DrawingSeriesDetail.as_view(),name='drawing_series-detail'),

]