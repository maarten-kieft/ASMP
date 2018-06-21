from datetime import datetime, timedelta
from django.db.models import Min, Max
from django.db.models.functions import Trunc
from core.models import Measurement, Meter, Statistic
import pytz

class MeasurementService:
    """"Class responsible for storing"""

    @staticmethod
    def save_measurement(parsed_message_result):
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
                power_usage_start=Min('power_usage_total_low') + Min('power_usage_total_normal'),
                power_usage_end=Max('power_usage_total_low') + Max('power_usage_total_normal'),
                power_supply_start=Min('power_supply_total_low') + Min('power_supply_total_normal'),
                power_supply_end=Max('power_supply_total_low') + Max('power_supply_total_normal'),
                gas_usage_start=Min('gas_usage_total'),
                gas_usage_end=Max('gas_usage_total'),
            )
        )

    @staticmethod
    def cleanup_measurements():
        """Cleaning up the measuments"""
        last_archived = Statistic.objects.all().aggregate(timestamp=Max('timestamp_end'))
        archive_threshold = pytz.utc.localize(datetime.now() - timedelta(hours=48))

        if last_archived["timestamp"] is not None and last_archived["timestamp"] < archive_threshold:
            archive_threshold = last_archived["timestamp"]

        Measurement.objects.filter(timestamp__lt=archive_threshold).delete()

    @staticmethod
    def get_measured_compoments():
        """Calculates an end date based on a start date and period"""
        latest_measurement = Measurement.objects.latest(field_name="timestamp")

        if(latest_measurement is not None):
            return {
                "has_gas" : latest_measurement.gas_usage_total > 0,
                "has_supply": latest_measurement.power_supply_total_low + latest_measurement.power_supply_total_normal > 0
            }

        return { "has_gas" : False, "has_supply": False}
        
    