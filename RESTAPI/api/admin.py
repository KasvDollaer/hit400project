from django.contrib import admin
from .models import FaultList, Employees, LoadShedding,Incidents

# Register your models here.
admin.site.register(FaultList)
admin.site.register(Employees)
admin.site.register(LoadShedding)
admin.site.register(Incidents)