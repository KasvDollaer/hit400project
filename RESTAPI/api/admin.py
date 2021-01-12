from django.contrib import admin
from .models import Fault_List, Employees, LoadShedding,Incidents

# Register your models here.
admin.site.register(Fault_List)
admin.site.register(Employees)
admin.site.register(LoadShedding)
admin.site.register(Incidents)