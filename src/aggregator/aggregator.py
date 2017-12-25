import time
from datetime import datetime, timedelta
from django.db.models import Max
from core.models import Statistic
from core.services.logservice import LogService
from core.services.measurementservice import MeasurementService
from core.services.statisticservice import StatisticService
from pytz import timezone
import pytz

class Aggregator:
    """"Class responsible for aggregating the received messages"""

    def start(self):
        """Execute aggregation and cleanup of the measurements"""
        while True:
            LogService.log_info("aggregator", "Creating statistics")
            self.create_statistics()
            LogService.log_info("aggregator", "Cleaning up")
            self.cleanup_measurements()
            LogService.log_info("aggregator", "Sleeping for 60 minutes")
            time.sleep(60*60)

    def create_statistics(self):
        """Aggregates the measurements into statistics"""
        now = datetime.now()
        min_timestamp = Statistic.objects.all().aggregate(Max('timestamp_end'))["timestamp_end__max"]
        max_timestamp = (now + ((datetime.min - now) % timedelta(minutes=60)) - timedelta(minutes=60)).replace(tzinfo=pytz.UTC)

        if min_timestamp is None:
            min_timestamp = datetime(2000, 1, 1, tzinfo=timezone('UTC'))

        aggregated_measurements = MeasurementService.get_aggregate_measurements(min_timestamp,max_timestamp)
        StatisticService.create_statistics(aggregated_measurements)

    def cleanup_measurements(self):
        MeasurementService.cleanup_measurements()
