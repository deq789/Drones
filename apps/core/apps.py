from django.apps import AppConfig
from threading import Thread
from datetime import datetime
import time
import os

WAIT_TIME_TO_CHECK = 60


class DroneBatteryThread(Thread):
    def run(self):
        from .models import Drone
        while True:
            # in case data folder does not exists or removed during runtime
            if not os.path.exists('data'):
                os.mkdir('data')
            info = self.get_drones_info(Drone)
            current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            message_header = '-'*10 + current_time + '-'*10 + '\n'
            with open('data/drone_batteries_log.txt', 'a') as f:
                f.write(message_header)
                f.write(info)
            time.sleep(WAIT_TIME_TO_CHECK)

    def get_drones_info(self, Drone):
        drone_batteries = Drone.objects.all().values_list(
            'serial_number', 'battery_percentage')
        info = ''
        for drone in drone_batteries:
            info += 'Serial number: ' + drone[0] + \
                ' Battery percentage: ' + str(drone[1]) + '\n'
        return info


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        DroneBatteryThread().start()
