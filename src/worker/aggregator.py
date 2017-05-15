import time
from django.db import connection
from web.models import Measurement, Statistic
from django.db.models.functions import Trunc, TruncMonth
from django.db.models import Min, Max, DateTimeField

class Aggregator:
    """"Class responsible for aggregating the received messages"""

    aggregateQuery = """
	INSERT INTO statistic (
		  meter_id
		, timestamp_start
		, timestamp_end
		, usage_start
		, usage_end
		, return_start
		, return_end
	)
	SELECT 
		  meter_id
		, timestamp
		, DATETIME(timestamp,'+60 minutes')
		, min(usage_total_low) + min(usage_total_normal) 
		, max(usage_total_low) + max(usage_total_normal) 
		, min(return_total_low) + min(return_total_normal)
		, max(return_total_low) + max(return_total_normal)
	FROM (
		select 
			  strftime('%Y-%m-%dT%H:00:00.000', timestamp) as timestamp
			, usage_current
			, usage_total_low
			, usage_total_normal
			, return_current
			, return_total_low
			, return_total_normal
			, meter_id
		FROM 
			measurement
	) as data
	WHERE
		timestamp < strftime('%Y-%m-%dT%H:00:00.000', datetime())
	GROUP BY 
		meter_id
		, timestamp
	"""

    """while True:
            with connection.cursor() as cursor:
                print("Aggregator: Performing cleanup")
                cursor.execute(self.cleanupQuery)
            with connection.cursor() as cursor:
                print("Aggregator: Aggregating results")
                cursor.execute(self.aggregateQuery)

            print("Aggregator: Sleeping for 30 mins")
            time.sleep(5)
            """

    cleanupQuery = """
        DELETE FROM measurement where timestamp < (SELECT max(timestamp_end) from statistic)
	"""

    def start(self):
        """Execute aggregation and cleanup of the measurements"""
        while True:
            self.create_statistics()

    def create_statistics(self):
        """Aggregates the measurements into statistics"""
        Statistic.objects.bulk_create(
            Measurement
            .objects
            .annotate(
                timestamp_start=Trunc('timestamp_start', 'day'),
                timestamp_end=Trunc('timestamp_end', 'day')
            )
            .values('timestamp_start', 'timestamp_end')
            .annotate(
                usage_start=Min('usage_start'),
                usage_end=Max('usage_end')
            )
        )

    def clean_measurements(self):
        """Cleaning up the measuments"""
        