from datetime import datetime
from django.utils.timezone import get_current_timezone
from dateutil.parser import parse
import pytz

class DateTimeParser:
    """Service to perform actions around date times"""

    @staticmethod
    def parse(date_string):
        """Parse a local datettime string and convert it to utc"""
        local_datetime = get_current_timezone().localize(parse(date_string))

        return local_datetime.astimezone(pytz.utc)
