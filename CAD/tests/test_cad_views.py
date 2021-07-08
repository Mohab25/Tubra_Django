from django.test import TestCase,Client
from django.urls import reverse 
from CAD.views import *
from CAD.models import *
from CAD.models import DrawingSeries, Drawing
from Aerodrome.models import Aerodrome
from Aerodrome_features.models import Aerodrome_Part,Aerodrome_Entity
from Employee.models import Employee
from django.core.files.uploadedfile import SimpleUploadedFile


class CADUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.c = Client()
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.aerodrome_1 = Aerodrome.objects.create(Name='PortSudan') 
        cls.img_path ='/home/mohab/Main Folder/Master degree/Research/Tubra/venv/Tubra/media/CAD/CAD1.jpg'
        cls.img = SimpleUploadedFile(name='cad_file.png', content=open(cls.img_path, 'rb').read(), content_type='image/png')
        cls.drawing_series_1= DrawingSeries.objects.create(name='series_1',Aerodrome=cls.aerodrome_1)
        cls.aerodrome_part_1 = Aerodrome_Part.objects.create(Name='part1',geom="POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))")
        cls.aerodrome_entity = Aerodrome_Entity.objects.create(Aerodrome=cls.aerodrome_1,Feature_Name='entity1',Aerodrome_Part_ID=cls.aerodrome_part_1,Category='aerodrome pavement')
        cls.employee_1= Employee.objects.create(First_Name='employee_1',Last_Name='employee_1_l',Password='test_pass',Role='manager',Current_employment_status='employee')
        cls.drawing_1= Drawing.objects.create(Title='cad1',CAD_file=cls.img,Number_of_issuance=3,Drawing_series=cls.drawing_series_1,Aerodrome_Entity=cls.aerodrome_entity,Author=cls.employee_1)

    def test_drawings_lists(self):
        res = self.c.get(reverse('drawing-list'))
        content = json.loads(res.content)
        self.assertTrue(len(content)>0)

    def test_drawing_series_list(self):
        res = self.c.get(reverse('drawing_series-list'))
        content = json.loads(res.content)
        self.assertTrue(len(content)>0)

    # def test_drawing_details(self):
    #     res = self.c.get('/CAD/drawing/1/')
    #     self.assertEquals(res.status_code,200)
    #     self.assertEquals(res.resolver_match.func.__name__,DrawingDetail.as_view().__name__)

    # def test_drawing_series_details(self):
    #     res = self.c.get('/CAD/drawing_series/1/')
    #     self.assertEquals(res.status_code,200)
    #     self.assertEquals(res.resolver_match.func.__name__,DrawingSeriesDetail.as_view().__name__)
