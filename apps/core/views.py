from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from apps.core.models import Drone, Medication
from .serializers import DroneSerializer, MedicationSerializer
from .utils import can_load_medication_weight, add_drone_to_medications


class StatusAPIView(APIView):
    def get(self, request):
        return Response({'status': 'working'})


class DroneRegisterAPIView(CreateAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class MedicationRegisterAPIView(APIView):
    def post(self, request):
        drone_serial_number = request.data['drone']
        medications = request.data['medications']
        drone = Drone.objects.get(serial_number=drone_serial_number)
        medications = add_drone_to_medications(drone, medications)

        if can_load_medication_weight(drone, medications):
            serializer = MedicationSerializer(data=medications, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({"medications": f"sum of medications weight must be less than drone weight limit of: {drone.weight_limit}"}, status=400)
