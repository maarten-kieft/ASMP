insert ignore into meter (name) values ({meter_name});

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
	(SELECT id FROM meter WHERE name = "{meter_name}"),
    now(),
	{usage_current},
    {usage_total_low},
    {usage_total_normal},
    {return_current},
    {return_total_low},
	{return_total_normal}
);