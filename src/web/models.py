from django.db import models

class Meter(models.Model):
    """The meter object"""
    name = models.CharField(max_length=80)

    class Meta:
        """Meta data class"""
        db_table = "Meter"


class Measurement(models.Model):
    """THe readings from the meter"""
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    usage_current = models.DecimalField(max_digits=10, decimal_places=3)
    usage_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    usage_total_normal = models.DecimalField(max_digits=10, decimal_places=3)
    return_current = models.DecimalField(max_digits=10, decimal_places=3)
    return_total_low = models.DecimalField(max_digits=10, decimal_places=3)
    return_total_normal = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        """Meta data class"""
        db_table = "Measurement"

class Statistic(models.Model):
    """Statistic based on the measurements"""
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    timestamp_start = models.DateTimeField()
    timestamp_end = models.DateTimeField()
    usage_start = models.DecimalField(max_digits=10, decimal_places=3)
    usage_end = models.DecimalField(max_digits=10, decimal_places=3)
    return_start = models.DecimalField(max_digits=10, decimal_places=3)
    return_end = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        """Meta data class"""
        db_table = "Statistic"
