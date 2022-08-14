from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Drone, Medication


class DroneSerializer(ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

    def create(self, validated_data):
        if self.validated_data['battery_percentage'] < 25 and self.validated_data['state'] == 'LOADING':
            raise ValidationError({"detail": "Drone can not be in loading state with battery percentage below 25%"})
        return super().create(validated_data)


class MedicationSerializer(ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
