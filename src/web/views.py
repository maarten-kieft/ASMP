from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Trunc
from django.db.models import Min, Max, DateTimeField, Q
from web.models import Measurement, Statistic
from pytz import timezone
import operator

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
    now = datetime.now()
    current = datetime(now.year, now.month, now.day, tzinfo=timezone('UTC'))
    previous = current + timedelta(days=-1)

    stats = (Statistic
             .objects
             .annotate(timestamp=Trunc('timestamp_start', 'day', output_field=DateTimeField()))
             .values('timestamp')
             .annotate(usage=Max('usage_end')-Min('usage_start')))

    cur_stats = list(filter(lambda s: s["timestamp"] == current, stats))
    prev_stats = list(filter(lambda s: s["timestamp"] == previous, stats))
    min_stats = list(sorted(stats, key=lambda s: s["usage"]))
    max_stats = list(sorted(stats, key=lambda s: s["usage"], reverse=True))

    model = {
        'current' : cur_stats[0] if len(cur_stats) > 0 else None,
        'previous': prev_stats[0] if len(prev_stats) > 0 else None,
        'min': min_stats[0] if len(min_stats) > 0 else None,
        'max': max_stats[0] if len(max_stats) > 0 else None
    }

    return JsonResponse(model, safe=False)

