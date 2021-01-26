from rest_framework import serializers
from .models import *

class FaultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaultList
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class LoadSheddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadShedding
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
