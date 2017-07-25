"""Generating fake measurements just for development and debugging purposes"""
from datetime import datetime
from dateutil import tz
import pytz
import time
from worker.parser import Parser
from worker.connector import Connector
from web.models import Meter, Measurement
import random

class Generator:
    """"Class responsible for generating measurements just for development and debugging purposes"""

    def start(self):
        """Starting the processor to listen for message, interpret and store them"""

        while True:
            measurement = self.generate_message()
            measurement.save()
            print("Storing new measurement")
            time.sleep(10)

    def generate_message(self):
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
