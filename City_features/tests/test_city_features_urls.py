from django.test import TestCase, Client
from City_features.models import *
from City_features.views import *
from Aerodrome.models import Aerodrome

class TestCityFeaturesUrls(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        cls.city_facility = City_Facility.objects.create(City_Name='Port Sudan',Facility_Name='Port Sudan Hospital',Description='City main hospital',Category='Healthcare',Aerodrome=cls.aerodrome,geom='POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))')
        cls.city_block = City_Blocks.objects.create(City_Name='Port Sudan',Block_Name='Block1',Block_Arabic_Name='بلوك1',Block_Number=1,Block_Class='class1',geom='MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)),((15 5, 40 10, 10 20, 5 10, 15 5)))')
        cls.city_street = City_Streets.objects.create(City_Name='Port Sudan',Street_Name='Street1',Street_Name_Arabic='شارع1',Street_Class='class1',Street_Class_Arabic='درجة اولى',geom='MULTILINESTRING ((10 10, 20 20, 10 40),(40 40, 30 30, 40 20, 30 10))' )
        cls.city_district = City_Districts.objects.create(City_Name='Port Sudan',District_Name='d1',District_Name_Arabic='مقاطعة1',District_Code='d',geom='MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)),((15 5, 40 10, 10 20, 5 10, 15 5)))')
        return super().setUpTestData()
    
    def test_facilities_urls(self):
        res = self.c.get('/City_Features/city_facilities/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Facilities_List.as_view().__name__)

    def test_facility_urls(self):
        res = self.c.get(f'/City_Features/city_facility/{self.city_facility.id}/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Facility_details.as_view().__name__)

    def test_blocks_urls(self):
        res = self.c.get('/City_Features/city_blocks/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Blocks_List.as_view().__name__)

    def test_block_urls(self):
        res = self.c.get(f'/City_Features/city_block/{self.city_block.id}/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Blocks_details.as_view().__name__)

    def test_streets_urls(self):
        res = self.c.get('/City_Features/city_streets/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Streets_List.as_view().__name__)

    def test_street_urls(self):
        res = self.c.get(f'/City_Features/city_street/{self.city_street.id}/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Streets_details.as_view().__name__)

    def test_districts_urls(self):
        res = self.c.get('/City_Features/city_districts/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Districts_List.as_view().__name__)

    def test_district_urls(self):
        res = self.c.get(f'/City_Features/city_district/{self.city_district.id}/')
        self.assertTrue(res.status_code==200)
        self.assertEquals(res.resolver_match.func.__name__,Districts_details.as_view().__name__)
