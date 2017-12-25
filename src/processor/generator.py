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
        measurement.power_usage_current = random.randint(300,400) / 1000
        measurement.power_usage_total_low = 0
        measurement.power_usage_total_normal = 0
        measurement.power_supply_current = random.randint(300,400) / 1000
        measurement.power_supply_total_low = 0
        measurement.power_supply_total_normal = 0
        measurement.timestamp = datetime.now(pytz.utc)

        if(measurement.power_usage_current < measurement.power_supply_current):
            measurement.power_usage_current = 0
        else :
            measurement.power_supply_current = 0

        return measurement
