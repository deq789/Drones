from django.contrib import admin
from django.urls import path, include
from .views import StatusAPIView, DroneRegisterAPIView

urlpatterns = [
    path('drones-register', DroneRegisterAPIView.as_view())
]
