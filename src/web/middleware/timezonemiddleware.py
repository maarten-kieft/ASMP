from tzlocal import get_localzone
from django.utils import timezone
from django.template import RequestContext, Template, loader, TemplateDoesNotExist
from django.http import HttpResponse

class TimeZoneMiddleware(object):
    """Sets the local time zone for each request"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timezone_string = request.COOKIES.get('asmp-timezone'); 
        
        if timezone_string is None:
            template = loader.get_template('init.html')
            context = {"test":"test"}

            return HttpResponse(template.render(context))

        timezone.activate(timezone_string)
        response = self.get_response(request)

        return response
       
