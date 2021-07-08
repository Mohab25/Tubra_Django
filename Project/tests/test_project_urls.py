from django.test import TestCase,Client
from Project.models import *
from Aerodrome.models import Aerodrome
from Project.views import *

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

    def test_project_lists_url(self):
        res = self.c.get('/Project/projects/')
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,ProjectsList.as_view().__name__)

    def test_project_details_url(self):
        res = self.c.get(f'/Project/project/{self.project.id}/')
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,ProjectDetails.as_view().__name__)