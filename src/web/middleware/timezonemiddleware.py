from tzlocal import get_localzone
from django.utils import timezone

class TimeZoneMiddleware(object):
    """Sets the local time zone for each request"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timezone.activate(get_localzone())
        response = self.get_response(request)

        return response
