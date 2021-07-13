from django.test import TestCase, Client
from Aerodrome.models import Aerodrome
from Aerodrome_features.models import *


class AerodromeFeaturesModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        cls.aerodrome_part = Aerodrome_Part.objects.create(Name='Aerorome part test',geom='POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))')
        cls.aerodrome_entity = Aerodrome_Entity.objects.create(Aerodrome=cls.aerodrome,Feature_Name='Test Feature',Aerodrome_Part_ID=cls.aerodrome_part,Category='Test Category', Elevation=45, geom='POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))', Entity_Condition='functioning', Description='')
        cls.pavement = Pavement_Construction.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Pavement_Name='Test Pavement', Width=45, Shoulder_Width=7.5, Pavement_Design_Type='r',Pavement_geom='MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)),((15 5, 40 10, 10 20, 5 10, 15 5)))')
        cls.utility_pole = Aerodrome_Utility_Pole.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Tension_Type='B',Cable_Size=1.25, Pole_Type='utility', Status='functioning', Remark='', Pole_geom='POINT (30 10)')
        cls.elect_cable = Aerodrome_Utility_Electric_Cable.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Cable_Size=1.25, Remark='', Cable_geom='LINESTRING (30 10, 10 30, 40 40)')
        cls.water_line = Aerodrome_Utility_Water_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Line_Size=1.25, Remark='', Line_geom='LINESTRING (30 10, 10 30, 40 40)')
        cls.gas_line = Aerodrome_Utility_Gas_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Line_Size=1.25, Remark='', Line_geom='LINESTRING (30 10, 10 30, 40 40)')
        cls.sewage_line = Aerodrome_Utility_Sewage_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity, Line_Size=1.25, Remark='', Line_geom='LINESTRING (30 10, 10 30, 40 40)')
        
        return super().setUpTestData()

    def test_models_creation(self):
        self.assertTrue(isinstance(self.aerodrome_part,Aerodrome_Part))
        self.assertTrue(isinstance(self.aerodrome_entity,Aerodrome_Entity))
        self.assertTrue(isinstance(self.pavement,Pavement_Construction))
        self.assertTrue(isinstance(self.utility_pole,Aerodrome_Utility_Pole))
        self.assertTrue(isinstance(self.elect_cable,Aerodrome_Utility_Electric_Cable))
        self.assertTrue(isinstance(self.water_line,Aerodrome_Utility_Water_Line))
        self.assertTrue(isinstance(self.gas_line,Aerodrome_Utility_Gas_Line))
        self.assertTrue(isinstance(self.sewage_line,Aerodrome_Utility_Sewage_Line))
