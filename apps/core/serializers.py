from rest_framework.serializers import ModelSerializer
from .models import Drone


class DroneSerializer(ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'
