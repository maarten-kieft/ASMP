from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Trunc
from django.db.models import Min, Max, DateTimeField, Q
from web.models import Measurement, Statistic
from pytz import timezone
import operator
from functools import reduce
from web.services.datetimeservice import DateTimeService

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
    avg_stats = len(stats) if reduce(lambda x, s: x+int(s["usage"]), stats, 0) else 0

    model = {
        'current' : cur_stats[0] if len(cur_stats) > 0 else None,
        'previous': prev_stats[0] if len(prev_stats) > 0 else None,
        'min': min_stats[0] if len(min_stats) > 0 else None,
        'max': max_stats[0] if len(max_stats) > 0 else None,
        'avg' : avg_stats / len(stats)
    }

    return JsonResponse(model, safe=False)

def get_overview_graph_data(request, period="year", start_date=None):
    """Return graph data based on the period"""
    start = DateTimeService.calculate_start_date(period) if start_date is None else  DateTimeService.parse(start_date)
    end = DateTimeService.calculate_end_date(start, period)

    stats = (Statistic
             .objects
             .annotate(timestamp=Trunc('timestamp_start', 'month', output_field=DateTimeField()))
             .values('timestamp')
             .annotate(usage=Max('usage_end')-Min('usage_start')))

    cur_stats = list(filter(lambda s: end >= s["timestamp"] >= start, stats))

    model = {
        'current':cur_stats
    }

    return JsonResponse(model, safe=False)

