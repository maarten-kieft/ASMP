from django.db import models

class Meter(models.Model):
    """The meter object"""
    name = models.CharField(max_length=80)

    class Meta:
        """Meta data class"""
        db_table = "Meter"


class Measurement(models.Model):
    """THe readings from the meter"""
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(db_index=True)
    power_usage_current = models.DecimalField(max_digits=10, decimal_places=3)
    power_usage_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    power_usage_total_normal = models.DecimalField(max_digits=10, decimal_places=3)
    power_supply_current = models.DecimalField(max_digits=10, decimal_places=3)
    power_supply_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    power_supply_total_normal = models.DecimalField(max_digits=10, decimal_places=3)
    gas_usage_total = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    gas_using_now = models.BooleanField(default=0)

    class Meta:
        """Meta data class"""
        db_table = "Measurement"

class Statistic(models.Model):
    """Statistic based on the measurements"""
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, db_index=True)
    timestamp_start = models.DateTimeField(db_index=True)
    timestamp_end = models.DateTimeField(db_index=True)
    power_usage_start = models.DecimalField(max_digits=10, decimal_places=3)
    power_usage_end = models.DecimalField(max_digits=10, decimal_places=3)
    power_supply_start = models.DecimalField(max_digits=10, decimal_places=3)
    power_supply_end = models.DecimalField(max_digits=10, decimal_places=3)
    gas_usage_start = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    gas_usage_end = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    class Meta:
        """Meta data class"""
        db_table = "Statistic"

class LogMessage(models.Model):
    """Log messages coming from the application""" 
    module = models.CharField(max_length=80)
    text = models.TextField()
    level = models.CharField(max_length=80)
    timestamp = models.DateTimeField(db_index=True)

    class Meta:
        """Meta data class"""
        db_table = "LogMessage"

class Setting(models.Model):
    """Settings of the application""" 
    name = models.CharField(max_length=80, primary_key=True)
    value = models.TextField()
    
    class Meta:
        """Meta data class"""
        db_table = "Setting"