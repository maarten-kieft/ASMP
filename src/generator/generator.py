import time
import random
from datetime import datetime
from core.models import Meter, Measurement
import pytz

class Generator:
    """"Class responsible for generating fake measurements just for development and debugging purposes"""

    def start(self):
        """Starting the generator to create messages"""

        while True:
            measurement = self.generate_message()
            measurement.save()
            print("Storing new measurement")
            time.sleep(10)

    def generate_message(self):
        """Genereates a new message"""
        meter = Meter.objects.get_or_create(name="4530303237303030303130313334353136")[0]

        measurement = Measurement()
        measurement.meter = meter
        measurement.usage_current = random.randint(300,400) / 1000
        measurement.usage_total_low = 0
        measurement.usage_total_normal = 0
        measurement.return_current = random.randint(300,400) / 1000
        measurement.return_total_low = 0
        measurement.return_total_normal = 0
        measurement.timestamp = datetime.now(pytz.utc)

        return measurement
