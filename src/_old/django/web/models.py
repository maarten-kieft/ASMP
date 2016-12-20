from django.db import models

class Meter(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=80)

class MeterMeasurement(models.Model):
    meter_id = models.ForeignKey(Meter,on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    usage_current = models.DecimalFieldld(max_digits=10, decimal_places=3)
    usage_total_low = models.DecimalFieldld(max_digits=10, decimal_places=3)
    usage_total_normal = models.DecimalFieldld(max_digits=10, decimal_places=3)
    return_current = models.DecimalFieldld(max_digits=10, decimal_places=3)
    return_total_low = models.DecimalFieldld(max_digits=10, decimal_places=3)
    return_total_normal = models.DecimalFieldld(max_digits=10, decimal_places=3)

