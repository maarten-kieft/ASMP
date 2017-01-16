from django.shortcuts import render
from django.http import HttpResponse
from web.models import MeterMeasurement, Meter

def index(request):
    measurements = MeterMeasurement.objects.order_by('-timestamp')[:1]

    return render(request,"index.html",{ 'model' : str(measurements[0].usage_current)})
    
#""Hello world:" + )
