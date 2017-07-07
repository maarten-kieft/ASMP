from datetime import datetime
from dateutil import tz
from dateutil.relativedelta import relativedelta
from django.utils.timezone import get_current_timezone

class DateTimeService:
    """Service to perform actions around date times"""

    @staticmethod
    def parse(date_string):
        """Calculates an end date based on a start date and period"""
        return datetime.strptime(date_string, '%Y-%m-%d').replace(tzinfo=get_current_timezone())

    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()
        timezone = get_current_timezone()

        if period == "month":
            return datetime(now.year, now.month, 1, tzinfo=timezone)

        if period == "day":
            return datetime(now.year, now.month, now.day, tzinfo=timezone)

        return  datetime(now.year, 1, 1, tzinfo=timezone)

    @staticmethod
    def calculate_end_date(start_date, period):
        """Calculates an end date based on a start date and period"""
        timezone = get_current_timezone()

        if period == "day":
            return start_date + relativedelta(days=1)

        if period == "month":
            return start_date + relativedelta(months=1)

        return  datetime(start_date.year, 12, 31, tzinfo=timezone)

    @staticmethod
    def calculate_interval(period):
        """Calculates an end date based on a start date and period"""
        if period == "day":
            return "hour"

        if period == "month":
            return "day"

        return "month"
