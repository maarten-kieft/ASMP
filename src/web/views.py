from django.shortcuts import render
from django.http import JsonResponse
from web.models import Measurement, Statistic
from django.db.models.functions import Trunc
from django.db.models import Min, Max, DateTimeField


def dashboard(request):
    """Returns the dashboard"""
    model = {
        'lastMeasurements' : Measurement.objects.order_by('-timestamp')[:10]
    }

    return render(request, "dashboard.html", {'model' : model})

def get_last_current_usage(request):
    """Returns the last know current usage"""
    last_measurement = Measurement.objects.order_by('-timestamp').first()
    model = {'timestamp':None, 'currentUsage':0}

    if last_measurement is not None:
        model = {
            'timestamp':last_measurement.timestamp,
            'currentUsage':last_measurement.usage_current
        }

    return JsonResponse(model)

def get_statistics(request):
    """Return statistics based on the period"""

    statistics = Statistic.objects.annotate(timestamp=Trunc('timestamp_start', 'day'), usage=Max('usage_end') - Min('usage_start'))
    
    #model = [
    #    {'timestamp' : statistics[0].timestamp, 'usage':statistics[0].usage},
    #    {'timestamp' : statistics[1].timestamp, 'usage':statistics[1].usage},
    #]

    model = [
        {'timestamp' : statistics[20].timestamp, 'usage' : statistics[20].usage},
    ]

    return JsonResponse(model,safe=False)

