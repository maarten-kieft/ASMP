INSERT INTO meter_measurement(
	meter_id,
    timestamp,
    usage_current,
    usage_total_low,
    usage_total_normal,
    return_current,
    return_total_low,
    return_total_normal
) VALUES (
	1,
    now(),
	1,
	1,
	1,
	1,
	1,
	{return_total_normal}
);