from django.urls import path,re_path
from .views import AerodromeFeaturesListView 

urlpatterns=[
    path('features/',AerodromeFeaturesListView.as_view(),name='Aerodrome Features'),
    
]