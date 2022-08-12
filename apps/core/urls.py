from django.urls import path
from .views import StatusAPIView, DroneRegisterAPIView, MedicationLoadAPIView, \
    MedicationCheckAPIView, DroneDetailPIView

urlpatterns = [
    path('drones/', DroneRegisterAPIView.as_view()),
    path('drones/<pk>/', DroneDetailPIView.as_view()),
    path('drones/load-medication', MedicationLoadAPIView.as_view()),
    path('drones/check-medication/<pk>/', MedicationCheckAPIView.as_view())
]
