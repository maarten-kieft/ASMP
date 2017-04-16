from django.db import models

class Meter(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = "Meter"


class Measurement(models.Model):
    meter = models.ForeignKey(Meter,on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    usage_current = models.DecimalField(max_digits=10, decimal_places=3)
    usage_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    usage_total_normal = models.DecimalField(max_digits=10, decimal_places=3)
    return_current = models.DecimalField(max_digits=10, decimal_places=3)
    return_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    return_total_normal = models.DecimalField(max_digits=10, decimal_places=3)
    aggregated = models.BooleanField(default='0')
    
    class Meta:
        db_table = "Measurement"