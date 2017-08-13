from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from django.utils.timezone import get_current_timezone
import pytz

class DateTimeService:
    """Service to perform actions around date times"""

    @staticmethod
    def parse(date_string):
        """Parse a local datettime string and convert it to utc"""
        local_datetime = get_current_timezone().localize(parse(date_string))
        
        return local_datetime.astimezone(pytz.utc)
        
    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()
        month = now.month if period != "year" else 1
        day = now.day if period == "day" else 1 

        return get_current_timezone().localize(datetime(now.year, month, day)).astimezone(pytz.utc)

    @staticmethod
    def calculate_end_date(start_date, period, backwards=False):
        """Calculates an end date based on a start date and period"""
        amount = -1 if backwards else 1
        local_start_date = start_date.astimezone( get_current_timezone())
        local_end_date = local_start_date + relativedelta(years=amount)
        
        if period == "day":
            local_end_date = local_start_date + relativedelta(days=amount)

        if period == "month":
            local_end_date = local_start_date + relativedelta(months=amount)
            
        return  local_end_date.astimezone(pytz.utc)

    @staticmethod
    def calculate_interval(period):
        """Calculates interval based on a period"""
        if period == "day":
            return "hour"

        if period == "month":
            return "day"

        return "month"
