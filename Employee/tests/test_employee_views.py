from django.test import TestCase, Client
from django.urls import reverse
from Employee.models import *
import json

class EmployeeViewsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client()
        return super().setUpClass()
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.employee = Employee.objects.create(First_Name='employee',Last_Name='employee_l',Password='test_pass',Role='manager',Current_employment_status='employee')
        return super().setUpTestData()

    def test_employee_list_view(self):
        res = self.c.get('/Employees/')
        content = json.loads(res.content)
        self.assertTrue(len(content)>0)

    def test_employee_details_view(self):
        res = self.c.get(reverse('employee-detail',kwargs={'pk':self.employee.id}))
        content = json.loads(res.content)
        self.assertEquals((content['id'],content['First_Name']),(self.employee.id,'employee'))