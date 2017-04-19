import time
from django.db import connection

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

    cleanupQuery = """
	DELETE 
	FROM measurement 
	where id in (
		SELECT m.id
		FROM
		measurement m 
		INNER JOIN statistic s ON CAST(strftime('%s', m.timestamp) as integer) BETWEEN CAST(strftime('%s', s.timestamp_start) as integer) AND CAST(strftime('%s', s.timestamp_end) as integer)
		LIMIT 1000
	)
	"""

    def start(self):
        """Execute aggregation and cleanup of the measurements"""
        while True:
            with connection.cursor() as cursor:
                perform_ceanup = True

                while perform_ceanup:
                    print("Performing cleanup")
                    cursor.execute(self.cleanupQuery)

                    if cursor.rowcount < 1000:
                        perform_ceanup = False

                print("Aggregating results")
                cursor.execute(self.aggregateQuery)
                print("Sleeping for 30 mins")
            time.sleep(5)

