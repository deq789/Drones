from django.contrib import admin
from django.urls import path, include
from .views import StatusAPIView, DroneRegisterAPIView, MedicationRegisterAPIView

urlpatterns = [
    path('drones-register', DroneRegisterAPIView.as_view()),
    path('drones-load-medication', MedicationRegisterAPIView.as_view())
]
