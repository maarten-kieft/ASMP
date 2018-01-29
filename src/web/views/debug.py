from django.shortcuts import render
from core.services.applicationservice import ApplicationService

def index(request):
    """Returns the debug screen"""

    model = {
        'message_format' : ApplicationService.get_meter_message_format()
    }

    return render(request, "debug.html", model)
