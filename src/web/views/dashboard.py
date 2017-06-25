from django.shortcuts import render
from django.http import JsonResponse
from web.services.datetimeservice import DateTimeService
from web.services.statisticservice import StatisticService
from web.models import Measurement

def index(request):
    """Returns the dashboard"""

    return render(request, "dashboard.html")

def get_last_current_usage(request, amount = "1"):
    """Returns the last know current usage"""
    model = []
    last_measurements = Measurement.objects.order_by('-timestamp')[:int(amount)]

    if last_measurements is None:
        return JsonResponse([{'timestamp':None, 'current_usage':0}], safe=False)

    for measurement in reversed(last_measurements):
        model.append({'timestamp':measurement.timestamp, 'currentUsage':measurement.usage_current})

    return JsonResponse(model, safe=False)

def get_statistics(request):
    """Return statistics based on the period"""
    day_statistics = StatisticService.get_summerized_statistics("day")

    return JsonResponse(day_statistics, safe=False)

def get_overview_graph_data(request, period="year", start_date=None):
    """Return graph data based on the period"""
    start = DateTimeService.calculate_start_date(period) if start_date is None else DateTimeService.parse(start_date)
    end = DateTimeService.calculate_end_date(start, period)
    stats = StatisticService.get_aggregated_statistics(DateTimeService.calculate_interval(period))

    model = {
        'data': list(filter(lambda s: end >= s["timestamp"] >= start, stats))
    }

    return JsonResponse(model, safe=False)

