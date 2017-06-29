from datetime import datetime
from pytz import timezone
from dateutil import tz
import pytz

class DateTimeService:
    """Service to perform actions around date times"""
    @staticmethod
    def parse(date_string):
        """Calculates an end date based on a start date and period"""
        local_time_zone = tz.tzlocal()
        
        return datetime.strptime(date_string, '%Y-%m-%d').replace(tzinfo=local_time_zone)

    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()
        local_time_zone = tz.tzlocal()
        if period == "month":
            return datetime(now.year, now.month, 1, tzinfo=local_time_zone)

        if period == "day":
            return datetime(now.year, now.month, now.day, tzinfo=local_time_zone)

        return  datetime(now.year, 1, 1, tzinfo=local_time_zone)

    @staticmethod
    def calculate_end_date(start_date, period):
        """Calculates an end date based on a start date and period"""
        local_time_zone = tz.tzlocal()

        if period == "day":
            return datetime(start_date.year, start_date.month, start_date.day+1, tzinfo=local_time_zone)

        if period == "month":
            return datetime(start_date.year, start_date.month+1, 1, tzinfo=local_time_zone)

        return  datetime(start_date.year, 12, 31, tzinfo=local_time_zone)

    @staticmethod
    def calculate_interval(period):
        """Calculates an end date based on a start date and period"""
        if period == "day":
            return "hour"

        if period == "month":
            return "day"

        return "month"
