from django.contrib import admin
from django.urls import path, include
from .views import StatusAPIView, DroneRegisterAPIView, MedicationLoadAPIView, \
    MedicationCheckAPIView, DroneCheckAvailableAPIView

urlpatterns = [
    path('drones/register', DroneRegisterAPIView.as_view()),
    path('drones/load-medication', MedicationLoadAPIView.as_view()),
    path('drones/check-medication/<str:drone_serial_number>',
         MedicationCheckAPIView.as_view()),
    path('drones/check-available', DroneCheckAvailableAPIView.as_view()),
]
