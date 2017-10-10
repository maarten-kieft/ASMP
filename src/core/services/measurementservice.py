from datetime import datetime, timedelta
from django.db.models import Min, Max
from django.db.models.functions import Trunc
from core.models import Measurement, Meter
import pytz

class MeasurementService:
    """"Class responsible for storing"""

    @staticmethod
    def save_measurement(self, parsed_message_result):
        """Interpret the parsed message"""
        meter = Meter.objects.get_or_create(name=parsed_message_result["meter_name"])[0]

        del parsed_message_result["meter_name"]
        measurement = Measurement(**parsed_message_result)
        measurement.meter = meter
        measurement.timestamp = datetime.now(pytz.utc)
        measurement.save()

    @staticmethod
    def get_aggregate_measurements(min_timestamp, max_timestamp):
        return (Measurement
            .objects
            .filter(timestamp__gt=min_timestamp,timestamp__lt=max_timestamp)
            .annotate(timestamp_start=Trunc('timestamp', 'hour'))
            .values('timestamp_start', 'meter_id')
            .annotate(
                usage_start=Min('usage_total_low') + Min('usage_total_normal'),
                usage_end=Max('usage_total_low') + Max('usage_total_normal'),
                return_start=Min('return_total_low') + Min('return_total_normal'),
                return_end=Max('return_total_low') + Max('return_total_normal')
            )
        )

    @staticmethod
    def cleanup_measurements(self):
        """Cleaning up the measuments"""
        last_archived = Statistic.objects.all().aggregate(timestamp=Max('timestamp_end'))
        archive_threshold = datetime.now() - timedelta(hours=48)

        if last_archived["timestamp"] is not None and last_archived["timestamp"] < archive_threshold:
            archive_threshold = last_archived["timestamp"]

        Measurement.objects.filter(timestamp__lt=archive_threshold).delete()
