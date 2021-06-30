from django.test import TestCase
from Employee.models import Employee

class EmployeeModelsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.First_Name = 'emp1'
        cls.Last_Name = 'emp1'
        cls.Password = 'pass'
        cls.Role = 'eng'
        cls.Current_employment_status = 'active'

    def test_model_creation(self):
        emp1 = Employee.objects.create(First_Name=self.First_Name,Last_Name=self.Last_Name,Password=self.Password,Role=self.Role,Current_employment_status=self.Current_employment_status)
        self.assertTrue(isinstance(emp1,Employee))