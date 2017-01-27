from django.shortcuts import render
from django.http import HttpResponse
from web.models import MeterMeasurement, Meter

def dashboard(request):
    measurements = MeterMeasurement.objects.order_by('-timestamp')[:1]


    meter = Meter()
    meter.name = "4530303237303030303130313334353136"
    meter.id = 10

    measurement = MeterMeasurement()
    measurement.meter = meter
    measurement.usage_current = 9.99
    measurement.usage_total_low = 8.88
    measurement.usage_total_normal = 2.33
    measurement.return_current = 2.34
    measurement.return_total_low = 2.33
    measurement.return_total_normal = 3.33

    measurement.save()

    return render(request, "dashboard.html", {'model' : str(measurements[0].usage_current)})
