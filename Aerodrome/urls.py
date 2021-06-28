from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('',AerodromesListView.as_view(),name='aerodrome-list'),
    re_path(r'aerodrome/(?P<pk>\d+)/$',AerodromeDetailsView.as_view(),name='aerodrome-detail'),
]