from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FaultList, LoadShedding, Incident, Employee
from .forms import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#regular views for the clerk

def ListPage(request):
    faults = FaultList.objects.all()
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
     'resolved': resolvedFaults,
     'incidents': incidents,
     'LoadSheddings': LoadSheddings,
     'AddFault': form,
    })

def FaultDetails(request, id):
    Fault = get_object_or_404(FaultList, id=id)
  


    if Fault.Status == 'Current' and request.method == 'POST':
        Form = AddFaultForm(data=request.POST)
        if Form.is_valid():
            Form.save()
    elif Fault.Status == 'New' and request.method == 'GET':
        Form = AddFaultForm()
        Form.Status = 'Current'



        # Fault.Status = 'Current'


    #use this view for both editing and details
    return render(request, 'clerk/views/faultdetail.html', {'Fault': Fault, 'form': Form})


def IncidentsDetails(request, id):
    Incidents = get_object_or_404(Incident, id=id)
    #use this view for viewing fault details
    return render(request, 'clerk/views/Incidents.html', {'Incidents': Incidents})


def LoadSheddingDetails(request, id):
    LoadSheddings = get_object_or_404(LoadShedding, id=id)
    return render(request, 'clerk/views/LoadShedding.html', {'LoadShedding': LoadSheddings})        
#Api views for Mobile App