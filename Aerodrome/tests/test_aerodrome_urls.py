from django.test import TestCase,Client
from django.urls import reverse 
from Aerodrome.models import Aerodrome
from Aerodrome.views import AerodromesListView, AerodromeDetailsView


class AerodromeUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.c = Client()
        cls.aerodrome_1 = Aerodrome.objects.create(Name='PortSudan') 

    def test_aerodrome_lists(self):
        res = self.c.get('/Aerodromes/')
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.resolver_match.func.__name__,AerodromesListView.as_view().__name__)

    def test_aerodrome_details(self):
        # the id is 2 because it's affected by other tests i.e 'models tests'
        res = self.c.get(f'/Aerodromes/aerodrome/{self.aerodrome_1.id}/')
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.resolver_match.func.__name__,AerodromeDetailsView.as_view().__name__)
