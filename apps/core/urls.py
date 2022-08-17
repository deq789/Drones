from django.urls import path
from .views import StatusAPIView, DroneRegisterAPIView, MedicationLoadAPIView, \
    MedicationCheckAPIView, DroneDetailPIView

urlpatterns = [
    path('drones/', DroneRegisterAPIView.as_view(), name='drones'),
    path('drones/<pk>/', DroneDetailPIView.as_view(), name='drones-detail'),
    path('drones/load-medication', MedicationLoadAPIView.as_view(),
         name='drones-load-medication'),
    path('drones/check-medication/<pk>/', MedicationCheckAPIView.as_view(),
         name='drones-check-medication')
]
