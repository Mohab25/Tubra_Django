from django.urls import path,re_path
from .views import *

urlpatterns=[
    path('features/',AerodromeFeaturesListView.as_view(),name='Aerodrome Features'),
    path('obeid_aerodrome_parts/',Obeid_Aerodrome_Parts.as_view(),name='Obeid_Aerodrome_Parts'),
    re_path(r'feature/(?P<pk>\d+)/$',AerodromeFeaturesDetailsView.as_view(),name='aerodrome_entity-detail'),
    #path('features_poi/',AerodromeFeaturesPOI.as_view(),name='Aerodrome Features POIs'),
    path('pavements/',AerodromeFeaturesPavementConstructions.as_view(),name='pavement-constructions'),   
    re_path(r'pavement/(?P<pk>\d+)/$',AerodromeFeaturesPavementConstructionDetails.as_view(),name='pavement-construction-details'),   
    re_path(r'fields_for_vector_creation/(?P<modelName>\w+)/$',get_fields_name_for_forms,name='fields_name_for_vector_creation'),   
    re_path(r'vector_creation/create/',add_aerodrome_features,name='add-aerodrome-features '),
    path('pois/',POIsView.as_view(),name='pois'),   

]

