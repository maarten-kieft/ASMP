class Aggregator:
    """"Class responsible for aggregating the received messages"""

    aggregateQuery = """
	INSERT INTO (
		meter_id
		, timestamp
		, usage_current
		, usage_total_low
		, usage_total_normal
		, return_current
		, return_total_low
		, return_total_normal
		, aggregated
	)
	SELECT 
		meter_id
		, timestamp
		, avg(usage_current)
		, max(usage_total_low)
		, max(usage_total_normal) 
		, avg(return_current)
		, max(return_total_low)
		, max(return_total_normal)
		, 1
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
			web_metermeasurement
		WHERE	
			aggregated = 0
	) as data
	GROUP BY 
		meter_id
		, timestamp
	"""

    cleanupQuery = """

	"""

    def run(self):
        with connection.cursor() as cursor:
            cursor.execute(aggregateQuery)

    
#1. je doet een groepering, 
#2. Je groeppeert op uur, pakt max van al die velden en avg van huidig.
#3. Je voegt die toe en verwijdert de source regels.
# dat doe je herhaal je tot er niks te doen is, daarna sleep je een uur
# di tmoet waars op een andere thread draaien

"""



SELECT 
	  meter_id
	, timestamp
	, max(usage_total_low) + max(usage_total_normal) usage_total
	, max(return_total_low) + max(return_total_normal) return_total
FROM (
	select 
		  strftime('%Y-%m-%dT%H:00:00.000', timestamp) as timestamp
		, usage_total_low
		, usage_total_normal
		, return_total_low
		, return_total_normal
		, meter_id
	FROM 
		web_metermeasurement
) as data
GROUP BY 
	  meter_id
	, timestamp

"""
