from django.test import TestCase
from Project.models import *
from Aerodrome.models import Aerodrome

class ProjectModelsTests(TestCase):
    @classmethod 
    def setUpTestData(cls) -> None:
        cls.aerodrome = Aerodrome.objects.create(Name='Port Sudan')
        cls.project = Project.objects.create(Project_Name='Test Project',Aerodrome=cls.aerodrome)

        cls.phase = Phase.objects.create(Project=cls.project,Phase_Name='Testing phase')
        
        cls.activity = Activity.objects.create(Phase=cls.phase,Activity_Name='Testing1',Completion=False)

        return super().setUpTestData()

    def test_project_models(self):
        self.assertTrue(isinstance(self.project,Project))
        self.assertTrue(isinstance(self.phase,Phase))
        self.assertTrue(isinstance(self.activity,Activity))
