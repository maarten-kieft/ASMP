from datetime import datetime, timedelta
from core.models import Measurement, Meter
import pytz

class MesasurementService:
    """"Class responsible for storing""""

    def save_measurement(self, parsed_message_result):
        """Interpret the parsed message"""
        meter = Meter.objects.get_or_create(name=parsed_message_result["meter_name"])[0]

        del parsed_message_result["meter_name"]
        measurement = Measurement(**parsed_message_result)
        measurement.meter = meter
        measurement.timestamp = datetime.now(pytz.utc)
        measurement.save()
