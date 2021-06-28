from .models import Employee
from .serializers import EmployeeListSerializer, EmployeeDetailsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Employee_List(ListCreateAPIView):
    model = Employee
    serializer_class = EmployeeListSerializer
    name = 'employee-list'

class Employee_Details(RetrieveUpdateDestroyAPIView):
    model = Employee
    serializer_class = EmployeeDetailsSerializer
    name = 'employee-details'