from rest_framework.serializers import ModelSerializer
from .models import Drone, Medication


class DroneSerializer(ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'


class MedicationSerializer(ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
