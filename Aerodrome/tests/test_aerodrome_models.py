from django.test import TestCase
from Aerodrome.models import Aerodrome

class AerodromeModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
       super().setUpClass()
       cls.aerodrome_1 = Aerodrome.objects.create(Name='PortSudan') 
      
    def test_creation(self):
        self.assertTrue(isinstance(self.aerodrome_1,Aerodrome))
