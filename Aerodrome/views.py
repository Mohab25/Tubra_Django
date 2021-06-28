from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Aerodrome
from .serializers import AerodromeListSerializer, AerodromeDetailsSerializer

class AerodromesListView(ListCreateAPIView):
    model = Aerodrome
    serializer_class = AerodromeListSerializer
    name = 'aerodrome-list'

class AerodromeDetailsView(RetrieveUpdateDestroyAPIView):
    model = Aerodrome
    serializer_class = AerodromeDetailsSerializer
    name = 'aerodrome-details'