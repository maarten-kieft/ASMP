from django.db.models.functions import Trunc
from django.db.models import Min, Max, DateTimeField, Q
from web.models import Statistic

class StatisticService:
    """Service to perform actions around statistics"""

    @staticmethod
    def get_aggregated_statistics(period):
        """Calculates an end date based on a start date and period"""
        return (Statistic
                .objects
                .annotate(timestamp=Trunc('timestamp_start', period, output_field=DateTimeField()))
                .values('timestamp')
                .annotate(usage=Max('usage_end')-Min('usage_start')))


