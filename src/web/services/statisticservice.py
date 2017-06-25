from datetime import datetime, timedelta, date
from pytz import timezone
from functools import reduce
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

    @staticmethod
    def get_summerized_statistics(period):
        """Calculates an end date based on a start date and period"""
        now = datetime.now()
        current = datetime(now.year, now.month, now.day, tzinfo=timezone('UTC'))
        previous = current + timedelta(days=-1)
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
            'avg' : avg_stats / len(stats)
        }

