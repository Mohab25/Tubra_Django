from django.test import TestCase,Client
from Project.models import *
from Aerodrome.models import Aerodrome
from Project.views import *
import json


class ProjectsUrlsTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()
    
    @classmethod 
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        cls.project = Project.objects.create(Project_Name='Test Project',Aerodrome=cls.aerodrome)

        cls.phase = Phase.objects.create(Project=cls.project,Phase_Name='Testing phase')
        
        cls.activity = Activity.objects.create(Phase=cls.phase,Activity_Name='Testing1',Completion=False)

        return super().setUpTestData()

    def test_project_lists_view(self):
        res = self.c.get('/Project/projects/')
        content = json.loads(res.content)
        self.assertTrue(len(content)>0)

    def test_project_details_url(self):
        res = self.c.get(f'/Project/project/{self.project.id}/')
        content = json.loads(res.content)
        self.assertTrue((content['id'],content['Project_Name']),(self.project.id,self.project.Project_Name))
