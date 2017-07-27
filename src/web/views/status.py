from django.shortcuts import render
from asmp.services.messageservice import MessageService

def index(request):
    """Returns the status screen"""

    recentMessages = MessageService.get_recent()

    return render(request, "status.html", {'model' : recentMessages})