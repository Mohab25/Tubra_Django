from .models import Employee
from .serializers import EmployeeListSerializer, EmployeeDetailsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Employee_List(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
    name = 'employee-list'

class Employee_Details(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailsSerializer
    name = 'employee-details'