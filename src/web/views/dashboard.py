from django.http import JsonResponse
from django.shortcuts import render
from core.models import Measurement
from core.services.statisticservice import StatisticService

def index(request):
    """Returns the dashboard"""

    model = {
        'day_stats' : StatisticService.get_statistics_summary("day"),
        'month_stats' : StatisticService.get_statistics_summary("month"),
        'year_stats' : StatisticService.get_statistics_summary("year")
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
            'powerCurrentUsage':measurement.power_usage_current,
            'powerCurrentSupply':measurement.power_supply_current
        })

    return JsonResponse(model, safe=False)

def get_overview_graph_data(request, period="year", start_date=None):
    """Return graph data based on the period"""

    model = {
        'data' : StatisticService.get_filtered_aggregated_statistics(period,start_date)
    }

    return JsonResponse(model, safe=False)
