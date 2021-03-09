from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FaultList, LoadShedding, Incident, Employee
from .forms import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
#regular views for the clerk

def ListPage(request):
    faults = FaultList.objects.filter(Status='new')
    current = FaultList.objects.fitlter(Status='current')
    resolvedFaults = FaultList.resolved.all()
    incidents = Incident.objects.all()
    LoadSheddings = LoadShedding.objects.all()
    
    if request.method == 'POST':
        form = AddFaultForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddFaultForm()
    return render(request, 'clerk/views/list.html', 
    {'faults': faults,
     'current': current,    
     'resolved': resolvedFaults,
     'incidents': incidents,
     'LoadSheddings': LoadSheddings,
     'AddFault': form,
    })

def FaultDetails(request, Fault_number):
    Fault = get_object_or_404(FaultList, Fault_number=Fault_number)
  
    form = FaultUpdateForm(instance=Fault)
    
    if request.method == 'POST':
        form = FaultUpdateForm(data=request.POST, instance=Fault)
        if form.is_valid():
            form.save()
            return redirect('/faults' )
        
    #use this view for both editing and details
    return render(request, 'clerk/views/faultdetail.html', {'Fault': Fault, 'form': form})


def IncidentsDetails(request, id):
    Incidents = get_object_or_404(Incident, id=id)

   
    #use this view for viewing fault details
    return render(request, 'clerk/views/Incidents.html', {'Incidents': Incidents})


def LoadSheddingDetails(request, id):
    LoadSheddings = get_object_or_404(LoadShedding, id=id)
    return render(request, 'clerk/views/LoadShedding.html', {'LoadShedding': LoadSheddings})        



#Api views for Mobile App

class FaultAPIView(APIView): #get all faults
    def get(self, request):
        faults = FaultList.objects.filter(Status='new')
        resolvedFaults = FaultList.resolved.all()
        faultserializer = FaultListSerializer(faults, many=True)
        rfaultserializer = FaultListSerializer(resolvedFaults, many=True)
        return Response(faultserializer.data + rfaultserializer.data)  #returning one serializer for now until i figure out how to do what i want
    def post(self, request):
        faultserializer = FaultListSerializer(data=request.data) #insert condition to only post new faults via the api
        if faultserializer.is_valid():
            faultserializer.save()
            return Response(faultserializer.data, status=status.HTTP_201_CREATED)
        return Response(faultserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FaultDetailsAPIView(APIView): #gets fault details
    def get_object(self, Fault_number):
        try:
            return FaultList.objects.get(Fault_number=Fault_number)
        
        except FaultList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, Fault_number):
        Fault = self.get_object(Fault_number)
        faultserializer = FaultListSerializer(Fault)
        return Response(faultserializer.data)
    def put(self, request, Fault_number):
        fault = self.get_object(Fault_number=Fault_number)
        serializer = FaultListSerializer(fault, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        fault = self.get_object(Fault_number)
        fault.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class IncidentAPIView(APIView): #get all incidents
    def get(self, request):
        incidents = Incident.objects.all()
        incidentserializer = IncidentSerializer(incidents, many=True)
        return Response(incidentserializer.data) 
    def post(self, request):
        incidentserializer = IncidentSerializer(data=request.data)
        if incidentserializer.is_valid():
            incidentserializer.save()
            return Response(incidentserializer.data, status=status.HTTP_201_CREATED)
        return Response(incidentserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncidentDetailsAPIView(APIView): #incident details
    def get_object(self, id):
        try:
            return Incident.objects.get(id=id)
        
        except FaultList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        incident = self.get_object(id)
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)
    def put(self, request, id):
        incident = self.get_object(id)
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        incident = self.get_object(id)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class LoadsheddingAPIView(APIView): #get all Loadshedding Schedules
    def get(self, request):
        LoadSheddings = LoadShedding.objects.all()
        serializer = LoadSheddingSerializer(LoadSheddings, many=True)
       
        return Response(serializer.data) #rfaultserializer.data])  #returning one serializer for now until i figure out how to do what i want
    # def post(self, request):
    #     load = LoadSheddingSerializer(data=request.data)
    #     if load.is_valid():
    #         load.save()
    #         return Response(load.data, status=status.HTTP_201_CREATED)
    #     return Response(load.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadsheddingDetailsAPIView(APIView): #loadshedding details
    def get_object(self, id):
        try:
            return LoadShedding.objects.get(id=id)
        
        except LoadShedding.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        loadshedding = self.get_object(id)
        serializer = LoadSheddingSerializer(loadshedding)
        return Response(serializer.data)
    # def put(self, request, id):
    #     fault = self.get_object(Fault_number)
    #     serializer = FaultListSerializer(fault, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, id):
    #     fault = self.get_object(Fault_number)
    #     fault.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)       