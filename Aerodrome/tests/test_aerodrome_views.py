from django.test import TestCase,Client
from django.urls import reverse 
from Aerodrome.models import Aerodrome


class CADUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.c = Client()
        cls.aerodrome_1 = Aerodrome.objects.create(Name='PortSudan') 

    def test_aerodrome_list_view(self):
        res = self.c.get('/Aerodromes/')
        content = res.json()
        self.assertEquals(len(content),1)

    def test_aerodrome_details_view(self):
        res = self.c.get(reverse('aerodrome-detail',kwargs={'pk':self.aerodrome_1.id}))
        content = res.json()
        self.assertEquals(content['Name'],'PortSudan')
