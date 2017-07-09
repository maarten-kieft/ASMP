from datetime import datetime, timedelta
from functools import reduce
from pytz import timezone
from django.db.models.functions import Trunc
from django.db.models import Min, Max
from django.utils.timezone import get_current_timezone
from dateutil.relativedelta import relativedelta
from web.models import Statistic
from web.services.datetimeservice import DateTimeService 

class StatisticService:
    """Service to perform actions around statistics"""

    @staticmethod
    def get_aggregated_statistics(period):
        """Calculates an end date based on a start date and period"""

        return (Statistic
                .objects
                .annotate(timestamp=Trunc('timestamp_start', period,tzinfo=get_current_timezone()))
                .values('timestamp')
                .annotate(usage=Max('usage_end')-Min('usage_start')))

    @staticmethod
    def get_summerized_statistics(period):
        """Calculates an end date based on a start date and period"""

        current = DateTimeService.calculate_start_date(period)
        previous = DateTimeService.calculate_previous(current,period)
        stats = StatisticService.get_aggregated_statistics(period)

        cur_stats = list(filter(lambda s: s["timestamp"] == current, stats))
        prev_stats = list(filter(lambda s: s["timestamp"] == previous, stats))
        min_stats = list(sorted(stats, key=lambda s: s["usage"]))
        max_stats = list(sorted(stats, key=lambda s: s["usage"], reverse=True))
        avg_stats = len(stats) if reduce(lambda x, s: x+int(s["usage"]), stats, 0) else 0

        return {
            'current' : cur_stats[0] if len(cur_stats) > 0 else None,
            'previous': prev_stats[0] if len(prev_stats) > 0 else None,
            'min': min_stats[0] if len(min_stats) > 0 else None,
            'max': max_stats[0] if len(max_stats) > 0 else None,
            'avg' : avg_stats / len(stats) if len(stats) > 0 else 0
        }
    
    @staticmethod
    def get_filtered_aggregated_statistics(period,start_date):
        """Get aggregated statistics for a certain period"""
        start = DateTimeService.calculate_start_date(period) if start_date is None else DateTimeService.parse(start_date)
        end = DateTimeService.calculate_end_date(start, period)
        stats = StatisticService.get_aggregated_statistics(DateTimeService.calculate_interval(period))

        return list(filter(lambda s: end >= s["timestamp"] >= start, stats))

