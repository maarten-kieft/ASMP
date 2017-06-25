from datetime import datetime
from pytz import timezone
import pytz

class DateTimeService:
    """Service to perform actions around date times"""
    @staticmethod
    def parse(date_string):
        """Calculates an end date based on a start date and period"""
        return datetime.strptime(date_string, '%Y-%m-%d').replace(tzinfo=pytz.utc)

    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()

        if period == "month":
            return datetime(now.year, now.month, 1, tzinfo=timezone('UTC'))

        if period == "day":
            return datetime(now.year, now.month, now.day, tzinfo=timezone('UTC'))

        return  datetime(now.year, 1, 1, tzinfo=timezone('UTC'))

    @staticmethod
    def calculate_end_date(start_date, period):
        """Calculates an end date based on a start date and period"""
        if period == "day":
            return datetime(start_date.year, start_date.month, start_date.day+1, tzinfo=timezone('UTC'))

        if period == "month":
            return datetime(start_date.year, start_date.month+1, 1, tzinfo=timezone('UTC'))

        return  datetime(start_date.year, 12, 31, tzinfo=timezone('UTC'))

    @staticmethod
    def calculate_interval(period):
        """Calculates an end date based on a start date and period"""
        if period == "day":
            return "hour"

        if period == "month":
            return "day"

        return "month"
