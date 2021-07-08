from django.test import TestCase
from Aerodrome.models import Aerodrome

class AerodromeModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        return super().setUpTestData()
    
    def test_aerodrome_object_creation(self):
        self.assertTrue(isinstance(self.aerodrome,Aerodrome))