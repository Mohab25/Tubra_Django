from django.urls import path,re_path
from .views import *
from .obeid_views import *

urlpatterns = [
    path('drawings/',DrawingList.as_view(),name='drawing-list'),
    path('drawing_series/',DrawingSeriesList.as_view(),name='drawing_series-list'),
    re_path(r'drawing/(?P<pk>\d+)/$',DrawingDetail.as_view(),name='drawing-detail'),
    re_path(r'drawing_series/(?P<pk>\d+)/$',DrawingSeriesDetail.as_view(),name='drawingseries-detail'),
    path('obeid_runway_layouts/',ObeidRunwayLayouts.as_view(),name='obeid_runway_layouts-list'),
    path('obeid_runway_markings/',ObeidRunwayMarkings.as_view(),name='obeid_runway_markings-list'),
    path('obeid_runway_profiles/',ObeidRunwayProfiles.as_view(),name='obeid_runway_profiles-list'),
    path('obeid_runway_cross_sections/',ObeidRunwayCrossSections.as_view(),name='obeid_runway_cross_sections-list'),
    path('obeid_runway_general/',ObeidRunwayGeneral.as_view(),name='obeid_runway_general-list'),
    path('obeid_taxiway_layouts/',ObeidTaxiwayLayouts.as_view(),name='obeid_taxiway_layouts-list'),
    path('obeid_taxiway_markings/',ObeidTaxiwayMarkings.as_view(),name='obeid_taxiway_markings-list'),
    path('obeid_taxiway_profiles/',ObeidTaxiwayProfiles.as_view(),name='obeid_taxiway_profiles-list'),
    path('obeid_taxiway_cross_sections/',ObeidTaxiwayCrossSections.as_view(),name='obeid_taxiway_cross_sections-list'),
    path('obeid_taxiway_general/',ObeidTaxiwayGeneral.as_view(),name='obeid_taxiway_general-list'),
    path('obeid_apron_layouts/',ObeidApronLayouts.as_view(),name='obeid_apron_layouts-list'),
    path('obeid_apron_markings/',ObeidApronMarkings.as_view(),name='obeid_apron_markings-list'),
    path('obeid_apron_profiles/',ObeidApronProfiles.as_view(),name='obeid_apron_profiles-list'),
    path('obeid_apron_cross_sections/',ObeidApronCrossSections.as_view(),name='obeid_apron_cross_sections-list'),
    path('obeid_apron_general/',ObeidApronGeneral.as_view(),name='obeid_apron_general-list'),
    path('obeid_drainage_layouts/',ObeidDrainageLayouts.as_view(),name='obeid_drainage_layouts-list'),
    path('obeid_drainage_markings/',ObeidDrainageMarkings.as_view(),name='obeid_drainage_markings-list'),
    path('obeid_drainage_profiles/',ObeidDrainageProfiles.as_view(),name='obeid_drainage_profiles-list'),
    path('obeid_drainage_cross_sections/',ObeidDrainageCrossSections.as_view(),name='obeid_drainage_cross_sections-list'),
    path('obeid_drainage_general/',ObeidDrainageGeneral.as_view(),name='obeid_drainage_general-list'),
    path('obeid_aerodrome_general/',ObeidAerodromeGeneral.as_view(),name='obeid_aerodrome_general-list'),


]
