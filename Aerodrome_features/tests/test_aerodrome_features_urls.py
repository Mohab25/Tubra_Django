from django.test import TestCase,Client , TransactionTestCase
from django.urls import reverse 
from  Aerodrome_features.models import *
from Aerodrome_features.views import *


class AerodromeUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.c = Client()
        cls.aerodrome = Aerodrome.objects.create(Name='PortSudan')
        cls.aerodrome_part = Aerodrome_Part.objects.create(Name='part1',geom="POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))")
        cls.aerodrome_entity = Aerodrome_Entity.objects.create(Aerodrome=cls.aerodrome,Feature_Name='entity1',Aerodrome_Part_ID=cls.aerodrome_part,Category='aerodrome place')

    def test_aerodrome_features_lists(self):
        res = self.c.get('/AerodromeFeatures/features/')
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.resolver_match.func.__name__,AerodromeFeaturesListView.as_view().__name__)

    def test_aerodrome_features_details(self):
        # the id is 2 because it's affected by other tests i.e 'models tests'
        res = self.c.get(f'/AerodromeFeatures/feature/{self.aerodrome_entity.id}/')
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.resolver_match.func.__name__,AerodromeFeaturesDetailsView.as_view().__name__)
