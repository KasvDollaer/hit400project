from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FaultList, LoadShedding, Incidents, Employees
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#regular views

def ListPage(request):
    faults = FaultList.objects.all()
    resolvedFaults = FaultList.resolved.all()
    incident = Incidents.objects.all()
    LoadShedding = LoadShedding.objects.all()
    return render(request, 'clerk/views/list.html', 
    {'faults': faults,
     'resolved': resolvedFaults,
     'incidents': incident,
     'LoadSheddings': LoadShedding,
    })

def FaultDetails(request, id):
    Fault = get_object_or_404(FaultList, id=id)
    return render(request, 'clerk/views/faultdetail.html', {'Fault': Fault})
#Api views