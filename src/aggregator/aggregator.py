from datetime import datetime, timedelta
from core.models import Measurement, Statistic, Meter
from core.services.messageservice import MessageService
from django.db.models.functions import Trunc
from django.db.models import Min, Max
from pytz import timezone
import pytz
import time

class Aggregator:
    """"Class responsible for aggregating the received messages"""

    def start(self):
        """Execute aggregation and cleanup of the measurements"""
        while True:
            MessageService.log_info("aggregator","Creating statistics")
            self.create_statistics()
            MessageService.log_info("aggregator","Sleeping for 1 minute")
            time.sleep(60)

    def create_statistics(self):
        """Aggregates the measurements into statistics"""
        now = datetime.now()
        min_timestamp = Statistic.objects.all().aggregate(Max('timestamp_end'))["timestamp_end__max"]
        max_timestamp = (now + ((datetime.min - now) % timedelta(minutes=60)) - timedelta(minutes=60)).replace(tzinfo=pytz.UTC)

        if min_timestamp is None:
            min_timestamp = datetime(2000, 1, 1, tzinfo=timezone('UTC'))

        query_set = (Measurement
                     .objects
                     .filter(
                         timestamp__gt=min_timestamp,
                         timestamp__lt=max_timestamp
                         )
                     .annotate(timestamp_start=Trunc('timestamp', 'hour'))
                     .values('timestamp_start', 'meter_id')
                     .annotate(
                         usage_start=Min('usage_total_low') + Min('usage_total_normal'),
                         usage_end=Max('usage_total_low') + Max('usage_total_normal'),
                         return_start=Min('return_total_low') + Min('return_total_normal'),
                         return_end=Max('return_total_low') + Max('return_total_normal'))
                    )

        statistics = [Statistic(
            meter=Meter.objects.filter(id=row["meter_id"]).first(),
            timestamp_start=row["timestamp_start"],
            timestamp_end=row["timestamp_start"] + timedelta(hours=1),
            usage_start=row["usage_start"],
            usage_end=row["usage_end"],
            return_start=row["return_start"],
            return_end=row["return_end"],
            ) for row in query_set]

        Statistic.objects.bulk_create(statistics)

    def clean_measurements(self):
        """Cleaning up the measuments"""

        cleanupQuery = "DELETE FROM measurement where timestamp < (SELECT max(timestamp_end) from statistic)"
        