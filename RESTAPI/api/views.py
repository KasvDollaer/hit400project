from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FaultList, LoadShedding, Incident, Employee
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
    return render(request, 'clerk/views/list.html', 
    {'faults': faults,
     'resolved': resolvedFaults,
     'incidents': incidents,
     'LoadSheddings': LoadSheddings,
    })

def FaultDetails(request, id):
    Fault = get_object_or_404(FaultList, id=id)
    #use this view for both editing and details
    return render(request, 'clerk/views/faultdetail.html', {'Fault': Fault})


def IncidentsDetails(request, id):
    Incidents = get_object_or_404(Incident, id=id)
    #use this view for viewing fault details
    return render(request, 'clerk/views/Incidents.html', {'Incidents': Incidents})


def LoadSheddingDetails(request, id):
    LoadSheddings = get_object_or_404(LoadShedding, id=id)
    return render(request, 'clerk/views/LoadShedding.html', {'LoadShedding': LoadSheddings})        
#Api views for Mobile App