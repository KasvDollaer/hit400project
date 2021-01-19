from rest_framework import serializers
from .models import *

class FaultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaultList
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class LoadSheddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadShedding
        fields = '__all__'

class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = '__all__'
