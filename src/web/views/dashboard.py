from django.shortcuts import render
from django.http import JsonResponse
from web.services.datetimeservice import DateTimeService
from web.services.statisticservice import StatisticService
from web.models import Measurement
import pytz

def index(request):
    """Returns the dashboard"""

    model = {
        'dayStats' : StatisticService.get_summerized_statistics("day"),
        'month_stats' : StatisticService.get_summerized_statistics("month"),
        'year_stats' : StatisticService.get_summerized_statistics("year")
    }

    return render(request, "dashboard.html", {'model' : model})

def get_last_measurements(request, amount="1"):
    """Returns the last know current usage"""

    last_measurements = Measurement.objects.order_by('-timestamp')[:int(amount)]
    model = []

    if last_measurements is None:
        model.append({'timestamp':None, 'current_usage':0})

    for measurement in reversed(last_measurements):
        model.append({
            'timestamp':measurement.timestamp,
            'currentUsage':measurement.usage_current
        })

    return JsonResponse(model, safe=False)

def get_overview_graph_data(request, period="year", start_date=None):
    """Return graph data based on the period"""
 
    start = DateTimeService.calculate_start_date(period) if start_date is None else DateTimeService.parse(start_date)
    end = DateTimeService.calculate_end_date(start, period)
    stats = StatisticService.get_aggregated_statistics(DateTimeService.calculate_interval(period))
    start_utc = start.astimezone(pytz.utc)
    end_utc = end.astimezone(pytz.utc)

    model = {
        'data': list(filter(lambda s: end_utc >= s["timestamp"] >= start_utc, stats))
    }

    return JsonResponse(model, safe=False)

