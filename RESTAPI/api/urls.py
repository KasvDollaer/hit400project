from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ListPage, name="Home"),
    # path('/faults/details', fault_details, name="fault_details")
    # path('/incidents/details', incidents_details, name="incidents_details")
    # # path('', homepage, name="Home")
    # path('', homepage, name="Home")
    # path('', homepage, name="Home")
]