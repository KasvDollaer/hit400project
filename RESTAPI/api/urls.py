from django.urls import path
from . import views
from .views import *

app_name = 'api'

urlpatterns = [
    path('', views.ListPage, name="Home"),
    path('<int:Fault_number>/', views.FaultDetails, name="fault_details"),
    #api urls
    path('api/Fault', FaultAPIView.as_view()),
    path("api/faultDetails", FaultDetailsAPIView.as_view()),  #add integers to urls
    path('api/incidents', IncidentAPIView.as_view()),
    path("api/incidentDetails", IncidentDetailsAPIView.as_view()),
    path('api/Loadshedding', LoadsheddingAPIView.as_view()),
    path("api/LoadsheddingDetails", LoadsheddingDetailsAPIView.as_view()),

    # path('/incidents/details', incidents_details, name="incidents_details")
    # # path('', homepage, name="Home")
    # path('', homepage, name="Home")
    # path('', homepage, name="Home")
]