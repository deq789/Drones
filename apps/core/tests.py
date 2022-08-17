from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.core.models import Medication, Drone


class DroneTests(APITestCase):
    def test_create_drone(self):
        """
        Ensure we can create a new drone object.
        """
        url = reverse('drones')
        data = {
            "serial_number": "serial-number-test-1",
            "model": "Lightweight",
            "weight_limit": "174",
            "battery_percentage": 40,
            "state": "LOADING"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drone.objects.count(), 1)
        self.assertEqual(Drone.objects.get().state, 'LOADING')
