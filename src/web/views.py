from django.shortcuts import render
from django.http import JsonResponse
from web.models import MeterMeasurement

def dashboard(request):
    """Returns the dashboard"""
    model = {
        'lastMeasurements' : MeterMeasurement.objects.order_by('-timestamp')[:10]
    }

    return render(request, "dashboard.html", {'model' : model})

def get_last_current_usage(request):
    """Returns the last know current usage"""
    last_measurement = MeterMeasurement.objects.order_by('-timestamp').first()

    model = {
        'timestamp':last_measurement.timestamp,
        'currentUsage':last_measurement.usage_current,
    }

    return JsonResponse(model)
