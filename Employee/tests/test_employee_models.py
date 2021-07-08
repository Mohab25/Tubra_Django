from django.test import TestCase, Client
from Employee.models import *

class EmployeeModelsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        #note with the creation the manyTomany fields are note tested.
        cls.employee = Employee.objects.create(First_Name='employee',Last_Name='employee_l',Password='test_pass',Role='manager',Current_employment_status='employee')
        return super().setUpTestData()

    def test_employee_models(self):
        self.assertTrue(isinstance(self.employee,Employee))