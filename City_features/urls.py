from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('city_facilities/',Facilities_List.as_view(),name='city_facility-list'),
    re_path(r'city_facility/(?P<pk>\d+)/$',Facility_details.as_view(),name='city_facility-detail'),
    path('city_blocks/',Blocks_List.as_view(),name='city_blocks-list'),
    re_path(r'city_block/(?P<pk>\d+)/$',Blocks_details.as_view(),name='city_blocks-detail'),
    path('city_streets/',Streets_List.as_view(),name='city_streets-list'),
    re_path(r'city_street/(?P<pk>\d+)/$',Streets_details.as_view(),name='city_streets-detail'),
    path('city_districts/',Districts_List.as_view(),name='city_districts-list'),
    re_path(r'city_district/(?P<pk>\d+)/$',Districts_details.as_view(),name='city_districts-detail'),
    path('obeid_districts/',Obeid_districts.as_view(),name='Obeid_districts-list'),
    path('obeid_streets/',Obeid_streets.as_view(),name='Obeid_streets-list'),
    path('obeid_urban_area/',Obeid_urban_areas.as_view(),name='Obeid_urban_areas-list'),

]