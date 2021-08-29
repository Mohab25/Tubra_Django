from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Drawing,DrawingSeries
from .serializers import DrawingsListSerializer, DrawingsDetailsSerializer, DrawingSeriesSerializer


class ObeidRunwayLayouts(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='runway', Drawing_category='L')
    serializer_class = DrawingsListSerializer
    name = 'obeid_runway_layouts-list'

class ObeidRunwayMarkings(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='runway', Drawing_category='M')
    serializer_class = DrawingsListSerializer
    name = 'obeid_runway_markings-list'

class ObeidRunwayProfiles(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='runway', Drawing_category='P')
    serializer_class = DrawingsListSerializer
    name = 'obeid_runway_profiles-list'

class ObeidRunwayCrossSections(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='runway', Drawing_category='C')
    serializer_class = DrawingsListSerializer
    name = 'obeid_runway__cross_sections-list'

class ObeidRunwayGeneral(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='runway', Drawing_category='G')
    serializer_class = DrawingsListSerializer
    name = 'obeid_runway__general-list'

class ObeidTaxiwayLayouts(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='taxiway', Drawing_category='L')
    serializer_class = DrawingsListSerializer
    name = 'obeid_taxiway_layouts-list'

class ObeidTaxiwayMarkings(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='taxiway', Drawing_category='M')
    serializer_class = DrawingsListSerializer
    name = 'obeid_taxiway_markings-list'

class ObeidTaxiwayProfiles(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='taxiway', Drawing_category='P')
    serializer_class = DrawingsListSerializer
    name = 'obeid_taxiway_profiles-list'

class ObeidTaxiwayCrossSections(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='taxiway',Drawing_category='C')
    serializer_class = DrawingsListSerializer
    name = 'obeid_taxiway__cross_sections-list'

class ObeidTaxiwayGeneral(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='taxiway', Drawing_category='G')
    serializer_class = DrawingsListSerializer
    name = 'obeid_taxiway__general-list'

class ObeidApronLayouts(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='apron', Drawing_category='L')
    serializer_class = DrawingsListSerializer
    name = 'obeid_apron_layouts-list'


class ObeidApronMarkings(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='apron', Drawing_category='M')
    serializer_class = DrawingsListSerializer
    name = 'obeid_apron_markings-list'

class ObeidApronProfiles(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='apron', Drawing_category='P')
    serializer_class = DrawingsListSerializer
    name = 'obeid_apron_profiles-list'

class ObeidApronCrossSections(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='apron',Drawing_category='C')
    serializer_class = DrawingsListSerializer
    name = 'obeid_apron__cross_sections-list'

class ObeidApronGeneral(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='apron', Drawing_category='G')
    serializer_class = DrawingsListSerializer
    name = 'obeid_apron__general-list'

class ObeidDrainageLayouts(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='drainage', Drawing_category='L')
    serializer_class = DrawingsListSerializer
    name = 'obeid_drainage_layouts-list'

class ObeidDrainageMarkings(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='drainage', Drawing_category='M')
    serializer_class = DrawingsListSerializer
    name = 'obeid_drainage_markings-list'

class ObeidDrainageProfiles(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='drainage', Drawing_category='P')
    serializer_class = DrawingsListSerializer
    name = 'obeid_drainage_profiles-list'

class ObeidDrainageCrossSections(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='drainage',Drawing_category='C')
    serializer_class = DrawingsListSerializer
    name = 'obeid_drainage__cross_sections-list'

class ObeidDrainageGeneral(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='drainage', Drawing_category='G')
    serializer_class = DrawingsListSerializer
    name = 'obeid_drainage__general-list'


class ObeidAerodromeGeneral(ListCreateAPIView):
    queryset = Drawing.objects.filter(aerodrome_part__Name__iexact='general', Drawing_category='G')
    serializer_class = DrawingsListSerializer
    name = 'obeid_aerodrome__general-list'