from django.test import TestCase, TransactionTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Aerodrome_features.models import *
from Aerodrome.models import Aerodrome

class AerodromeModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
       super().setUpClass()
       cls.aerodrome = Aerodrome.objects.create(Name='PortSudan')
       cls.aerodrome_part = Aerodrome_Part.objects.create(Name='part1',geom="POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))")
       cls.aerodrome_entity = Aerodrome_Entity.objects.create(Aerodrome=cls.aerodrome,Feature_Name='entity1',Aerodrome_Part_ID=cls.aerodrome_part,Category='aerodrome place')
       cls.pavement = Pavement_Construction.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Pavement_Name='test Apron',Width=350,Shoulder_Width=0,Pavement_Design_Type='r',Subgrade_Density=0.7, Subgrade_Soil_Classification='3@#3',Soil_Shear_Strength=0.5,Soil_DCP_Test_Result=0.5,Soil_CPT_Test_Result=0.2,Soil_Percolation_Rate=0.2,Pavement_geom='MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)),((15 5, 40 10, 10 20, 5 10, 15 5)))')
       cls.utilPole = Aerodrome_Utility_Pole.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Tension_Type='B',Cable_Size=2.2,Pole_Type='elect',Status='active',Remark='',Pole_geom='POINT (30 10)')
       cls.electCable =  Aerodrome_Utility_Electric_Cable.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Cable_Size=1.2,Remark='',Cable_geom='LINESTRING (30 10, 10 30, 40 40)')
       cls.waterLine  = Aerodrome_Utility_Water_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Line_Size=1.2,Remark='',Line_geom='LINESTRING (30 10, 10 30, 40 40)')
       cls.gasLine  = Aerodrome_Utility_Gas_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Line_Size=1.2,Remark='',Line_geom='LINESTRING (30 10, 10 30, 40 40)')
       cls.sewageLine  = Aerodrome_Utility_Sewage_Line.objects.create(Aerodrome_Entity=cls.aerodrome_entity,Line_Size=1.2,Remark='',Line_geom='LINESTRING (30 10, 10 30, 40 40)')
       cls.img_path ='/home/mohab/Main Folder/Master degree/Research/Tubra/venv/Tubra/media/CAD/CAD1.jpg'
       cls.img = SimpleUploadedFile(name='cad_file.png', content=open(cls.img_path, 'rb').read(), content_type='image/png')
       cls.Aerodrome_img = Aerodrome_Entity_Image.objects.create(Name='testing_img',Image=cls.img,Aerodrome_Entity=cls.aerodrome_entity)

    def test_aerodrome_entity_creation(self):
        self.assertTrue(isinstance(self.aerodrome_entity,Aerodrome_Entity))

    def test_aerodrome_pavement_creation(self):
        self.assertTrue(isinstance(self.pavement,Pavement_Construction))

    def test_aerodrome_utility_pole_creation(self):
        self.assertTrue(isinstance(self.utilPole,Aerodrome_Utility_Pole))

    def test_aerodrome_elect_cable_creation(self):
        self.assertTrue(isinstance(self.electCable,Aerodrome_Utility_Electric_Cable))

    def test_aerodrome_water_line_creation(self):
        self.assertTrue(isinstance(self.waterLine,Aerodrome_Utility_Water_Line))

    def test_aerodrome_gas_line_creation(self):
        self.assertTrue(isinstance(self.gasLine,Aerodrome_Utility_Gas_Line))

    def test_aerodrome_sewage_line_creation(self):
        self.assertTrue(isinstance(self.sewageLine,Aerodrome_Utility_Sewage_Line))

    def  test_aerodrome_entity_img(self):
        self.assertTrue(isinstance(self.Aerodrome_img,Aerodrome_Entity_Image))