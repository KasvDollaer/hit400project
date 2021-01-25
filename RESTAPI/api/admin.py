from django.contrib import admin
from .models import FaultList, Employee, LoadShedding,Incident

# Register your models here.
admin.site.register(FaultList)
admin.site.register(Employee)
admin.site.register(LoadShedding)
admin.site.register(Incident)