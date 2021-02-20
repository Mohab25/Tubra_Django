from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializer.ModelSerializer):
    class Meta:
        model = Employee
        fields='__all__'
