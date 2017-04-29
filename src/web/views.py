from django.shortcuts import render
from django.http import JsonResponse
from web.models import Measurement, Statistic
from django.db.models.functions import TruncMonth

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
    statistics = Statistic.objects.raw("""
        SELECT 
              min(id) as id
            , meter_id
            , timestamp as timestamp_start
            , DATETIME(timestamp,'+1 days') as timestamp_end
            , min(usage_start) as usage_start 
            , max(usage_end) as usage_end
            , min(return_start) as return_start
            , max(return_end) as return_end
        FROM (
            select 
                  id
                , strftime('%Y-%m-%dT00:00:00.000', timestamp_start) as timestamp
                , usage_start
                , usage_end
                , return_start
                , return_end
                , meter_id
            FROM 
                statistic
        ) as data
        WHERE
            timestamp in (
                strftime('%Y-%m-%dT00:00:00.000', datetime('NOW', '-60 days'))
                , strftime('%Y-%m-%dT00:00:00.000', datetime('NOW','-61 day'))
            ) 
        GROUP BY 
            meter_id
            , timestamp
        """)

    model = [
        {'timestamp' : statistics[0].timestamp_start, 'usage':statistics[0].usage_end - statistics[0].usage_start},
        {'timestamp' : statistics[1].timestamp_start, 'usage':statistics[1].usage_end - statistics[1].usage_start}
    ]

    return JsonResponse(model,safe=False)

