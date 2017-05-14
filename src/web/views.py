from django.shortcuts import render
from django.http import JsonResponse
from web.models import Measurement, Statistic
from django.db.models.functions import Trunc, TruncMonth
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

    #import pdb; pdb.set_trace()
    #statistics = Statistic.objects.filter(id=1).annotate(timestamp=Trunc('timestamp_start','day', output_field=DateTimeField())).values('timestamp').annotate(usage_start = Min('usage_start'))
    #s = Statistic.objects.filter(id=1)
    s = Statistic.objects.filter(id=1).annotate(timestamp=Trunc('timestamp_start','day')).values('timestamp').annotate(usage_start = Min('usage_start'))
    #model = [
    #    {'timestamp' : statistics[0].timestamp, 'usage':statistics[0].usage},
    #    {'timestamp' : statistics[1].timestamp, 'usage':statistics[1].usage},
    #]

    model = [
        {'timestamp' : s[0].timestamp},
    ]

    return JsonResponse(model,safe=False)

