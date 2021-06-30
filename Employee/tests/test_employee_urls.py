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
        
    def test_employees_list(self):
        res = self.c.get('/Employees/')
        self.assertEquals(res.status_code,200)
        self.assertEqual(res.resolver_match.func.__name__,Employee_List.as_view().__name__)

    def test_employee_details(self):
        #the first obj from model test will have id 1, then the obj will be deleted but the id will begin from 2  
        #res = self.c.get(reverse('employee-detail',kwargs={'pk':self.emp1.id}))
        res = self.c.get('/Employees/employee/2/')
        self.assertEquals(res.status_code,200)
        self.assertEqual(res.resolver_match.func.__name__,Employee_Details.as_view().__name__)