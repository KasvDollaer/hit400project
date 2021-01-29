from django import forms
from .models import FaultList, Incident, LoadShedding, Employee

class AddFaultForm(forms.ModelForm):   #rinobuda paZasi pemaFault lists
    class Meta:
        model = FaultList
        fields = ('Name', 'Location', 'Duration', 'Description')

# class FaultUpdateForm(forms.ModelForm):    #form rinobuda paFault Details
#     class Meta:
#         model = FaultList
#         fields = ('Status')

class LoadSheddingForm(forms.ModelForm):   #form rinobuda paLoadshedding page
    class Meta:
        model = LoadShedding
        fields = '__all__'
class IncidentForm(forms.ModelForm):   #form rinobuda paIncidents page
    class Meta:
        model = Incident
        exclude = ('Status',)
# class IncidentUpdateForm(forms.ModelForm):   #form rinobuda paIncidents page
#     class Meta:
#         model = Incident
#         fields = ('Status')
class AddWorkerForm(forms.ModelForm):  #form rekuAssigner worker to a Fault (internal matters)
    class Meta:
        model = Employee
        fields = ()