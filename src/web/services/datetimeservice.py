
from dateutil import tz
from dateutil.parser import *
from dateutil.relativedelta import relativedelta
from django.utils.timezone import get_current_timezone
from datetime import datetime
import pytz

class DateTimeService:
    """Service to perform actions around date times"""

    @staticmethod
    def parse(date_string):
        """Parse a local datettime string and convert it to utc"""
        local_datetime =  get_current_timezone().localize(parse(date_string))
        utc_datetime = local_datetime.astimezone(pytz.utc)
        
        return utc_datetime

    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()
        timezone = get_current_timezone()

        if period == "month":
            return datetime(now.year, now.month, 1, tzinfo=timezone).astimezone(pytz.utc)

        if period == "day":
            return datetime(now.year, now.month, now.day, tzinfo=timezone).astimezone(pytz.utc)

        return  datetime(now.year, 1, 1, tzinfo=timezone).astimezone(pytz.utc)

    @staticmethod
    def calculate_end_date(start_date, period):
        """Calculates an end date based on a start date and period"""

        if period == "day":
            return start_date + relativedelta(days=1)

        if period == "month":
            return start_date + relativedelta(months=1)

        return  start_date + relativedelta(years=1)

    @staticmethod
    def calculate_interval(period):
        """Calculates interval based on a period"""
        if period == "day":
            return "hour"

        if period == "month":
            return "day"

        return "month"
