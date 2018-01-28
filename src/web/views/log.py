from django.shortcuts import render
from core.services.logservice import LogService
from core.services.applicationservice import ApplicationService

def index(request):
    """Returns the status screen"""

    recent_messages = LogService.get_recent()
    label_types = {'info' : 'info', 'warning' : 'warning', 'success' : 'success', 'error' : 'danger'}
    model = {'messages' : recent_messages, 'label_types' : label_types, 'message_format' : ApplicationService.get_meter_message_format()}

    return render(request, "log.html", model)
