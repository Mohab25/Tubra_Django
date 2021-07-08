from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Aerodrome
from .serializers import AerodromeListSerializer, AerodromeDetailsSerializer

class AerodromesListView(ListCreateAPIView):
    queryset = Aerodrome.objects.all()
    serializer_class = AerodromeListSerializer
    name = 'aerodrome-list'

class AerodromeDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Aerodrome.objects.all()
    serializer_class = AerodromeDetailsSerializer
    name = 'aerodrome-detail'