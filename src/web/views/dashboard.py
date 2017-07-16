import pytz
from django.http import JsonResponse
from django.shortcuts import render

from web.models import Measurement
from web.services.datetimeservice import DateTimeService
from web.services.statisticservice import StatisticService
from django.utils.timezone import get_current_timezone

def index(request):
    """Returns the dashboard"""

    model = {
        'day_stats' : StatisticService.get_summerized_statistics("day"),
        'month_stats' : StatisticService.get_summerized_statistics("month"),
        'year_stats' : StatisticService.get_summerized_statistics("year"),
        'bla':get_current_timezone()
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

    model = {
        'data' : StatisticService.get_filtered_aggregated_statistics(period,start_date)
    }

    return JsonResponse(model, safe=False)
