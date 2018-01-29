from django.shortcuts import render
from core.services.logservice import LogService
from core.services.applicationservice import ApplicationService

def index(request):
    """Returns the log screen"""

    recent_messages = LogService.get_recent()
    label_types = {
        'info' : 'info',
        'debug' : 'info', 
        'warning' : 'warning', 
        'success' : 'success', 
        'error' : 'danger'
    }

    model = {
        'messages' : recent_messages, 
        'label_types' : label_types
    }

    return render(request, "log.html", model)
