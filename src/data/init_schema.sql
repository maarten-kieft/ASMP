create DATABASE if not exists asmp;

use asmp;

create table if not exists asmp.meter
(
    id int not null auto_increment,
    name varchar(80) not null,
    primary key(id)
);

create table if not exists asmp.meter_measurement
(
    meter_id int not null auto_increment,
    [timestamp] datetime not null,
	usage_current decimal not null,
	usage_total_low decimal not null,
	usage_total_normal decimal not null,
	return_current decimal not null,
	return_total_low decimal not null,
	return_total_normal decimal not null,
);