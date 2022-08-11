from rest_framework.views import APIView
from rest_framework.response import Response

from apps.core.models import Drone
from .serializers import DroneSerializer
from rest_framework.generics import CreateAPIView

class StatusAPIView(APIView):
    def get(self, request):
        return Response({'status': 'working'})

class DroneRegisterAPIView(CreateAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()

