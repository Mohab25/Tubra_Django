from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('features/',AerodromeFeaturesListView.as_view(),name='Aerodrome Features'),
    re_path(r'feature/(?P<pk>\d+)/$',AerodromeFeaturesDetailsView.as_view(),name='aerodrome_entity-detail'),
    path('features_poi/',AerodromeFeaturesPOI.as_view(),name='Aerodrome Features POIs'),
    path('pavement_constructions/',AerodromeFeaturesPavementConstructions.as_view(),name='pavement-constructions'),   
    re_path(r'pavement_construction/(?P<pk>\d+)/$',AerodromeFeaturesPavementConstructionDetails.as_view(),name='pavement-construction-details'),   
]

