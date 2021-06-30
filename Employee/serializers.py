from .models import Employee
from rest_framework import serializers

class EmployeeListSerializer(serializers.ModelSerializer):
    #employees = serializers.HyperlinkedRelatedField(read_only=True,view_name='employee-list')
    class Meta:
        model = Employee
        fields='__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = Employee 
        fields='__all__'