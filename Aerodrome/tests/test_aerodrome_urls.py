from django.test import TestCase, Client
from Aerodrome.models import Aerodrome
from Aerodrome.views import *

class AerodromeUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        return super().setUpTestData()
    
    def test_aerodromes_list_url(self):
        res = self.c.get('/Aerodromes/')
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,AerodromesListView.as_view().__name__)
    
    def test_aerodrome_details_url(self):
        res = self.c.get(f'/Aerodromes/aerodrome/{self.aerodrome.id}/')
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,AerodromeDetailsView.as_view().__name__)
    