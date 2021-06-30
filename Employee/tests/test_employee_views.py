from django.test import TestCase, Client
from django.urls import reverse
from Employee.models import Employee
from Employee.views import Employee_List, Employee_Details
import sys
class EmployeeModelsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.First_Name = 'emp1'
        cls.Last_Name = 'emp1'
        cls.Password = 'pass'
        cls.Role = 'eng'
        cls.Current_employment_status = 'active'
        cls.emp1 = Employee.objects.create(First_Name=cls.First_Name,Last_Name=cls.Last_Name,Password=cls.Password,Role=cls.Role,Current_employment_status=cls.Current_employment_status)
        cls.c = Client()
        
    def test_employees_list_view(self):
        res = self.c.get('/Employees/')
        content = res.json()
        self.assertEquals(len(content),1)

    def test_employee_details_view(self):
        res = self.c.get(reverse('employee-detail',kwargs={'pk':self.emp1.id}))
        content = res.json()
        self.assertEquals((content['First_Name'],content['Password'],content['Role']),('emp1','pass','eng'))