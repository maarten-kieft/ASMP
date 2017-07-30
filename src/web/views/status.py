from django.shortcuts import render
from asmp.services.messageservice import MessageService

def index(request):
    """Returns the status screen"""

    recent_messages = MessageService.get_recent()
    label_types = {'info' : 'info', 'warning' : 'warning', 'success' : 'success', 'error' : 'danger'}
    model = {'messages' : recent_messages, 'label_types' : label_types}

    return render(request, "status.html", model)
