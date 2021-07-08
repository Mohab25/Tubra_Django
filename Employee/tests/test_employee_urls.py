from django.test import TestCase, Client
from django.urls import reverse
from Employee.models import *
from Employee.views import *
import json

class EmployeeUrlsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.employee = Employee.objects.create(First_Name='employee',Last_Name='employee_l',Password='test_pass',Role='manager',Current_employment_status='employee')
        return super().setUpTestData()

    def test_employee_list_url(self):
        res = self.c.get('/Employees/')
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,Employee_List.as_view().__name__)

    def test_employee_details_url(self):
        res = self.c.get(reverse('employee-detail',kwargs={'pk':self.employee.id}))
        self.assertTrue(res.status_code,200)
        self.assertTrue(res.resolver_match.func.__name__,Employee_Details.as_view().__name__)
