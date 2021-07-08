from django.test import TestCase, Client
from Aerodrome.models import Aerodrome
from Aerodrome.views import *
import json


class AerodromeUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        return super().setUpTestData()
    
    def test_aerodromes_list_view(self):
        res = self.c.get('/Aerodromes/')
        content = json.loads(res.content)
        self.assertTrue(len(content)>0)
    
    def test_aerodrome_details_view(self):
        res = self.c.get(f'/Aerodromes/aerodrome/{self.aerodrome.id}/')
        content = json.loads(res.content)
        self.assertTrue(content['Name'],self.aerodrome.Name)
