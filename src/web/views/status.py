import pytz
from django.http import JsonResponse
from django.shortcuts import render

from web.models import Measurement
from web.services.datetimeservice import DateTimeService
from web.services.statisticservice import StatisticService
from django.utils.timezone import get_current_timezone

def index(request):
    """Returns the status screen"""


    return render(request, "status.html", {'model' : None})