from datetime import datetime
from pytz import timezone

class DateTimeService:
    """Service to perform actions around date times"""
    @staticmethod
    def parse(date_string):
        """Calculates an end date based on a start date and period"""
        now = datetime.now()

        return  datetime(now.year, 1, 1, tzinfo=timezone('UTC'))

    @staticmethod
    def calculate_start_date(period):
        """Calculates a start date based on a period"""
        now = datetime.now()

        return  datetime(now.year, 1, 1, tzinfo=timezone('UTC'))

    @staticmethod
    def calculate_end_date(start_date, period):
        """Calculates an end date based on a start date and period"""
        now = datetime.now()

        return  datetime(now.year, now.month, now.day, tzinfo=timezone('UTC'))
