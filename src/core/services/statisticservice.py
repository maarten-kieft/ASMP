from functools import reduce
from datetime import timedelta
from django.db.models.functions import Trunc
from django.db.models import Min, Max
from django.utils.timezone import get_current_timezone, make_aware
from core.models import Statistic, Meter
from core.calculation.periodcalculator import PeriodCalculator
from core.parsing.datetimeparser import DateTimeParser
import pytz

class StatisticService:
    """Service to perform actions around statistics"""

    @staticmethod
    def create_statistics(aggregated_measurements):
        statistics = [Statistic(
            meter= Meter.objects.filter(id=row["meter_id"]).first(),
            timestamp_start=row["timestamp_start"],
            timestamp_end=row["timestamp_start"] + timedelta(hours=1),
            power_usage_start=row["power_usage_start"],
            power_usage_end=row["power_usage_end"],
            power_supply_start=row["power_supply_start"],
            power_supply_end=row["power_supply_end"],
            gas_usage_start=row["gas_usage_start"],
            gas_usage_end=row["gas_usage_end"]
        ) for row in aggregated_measurements]

        Statistic.objects.bulk_create(statistics)

    @staticmethod
    def get_aggregated_statistics(period, start = None, end = None):
        """Calculates an end date based on a start date and period"""
        resultSet = Statistic.objects.all()

        if start is not None and end is not None:
            resultSet = Statistic.objects.filter(timestamp_start__range=(start, end))

        return (resultSet
                .annotate(timestamp=Trunc('timestamp_start', period,tzinfo=get_current_timezone()))
                .values('timestamp')
                .annotate(
                    total_usage=Max('power_usage_end')-Min('power_usage_start'),
                    total_return=Max('power_supply_end')-Min('power_supply_start')
                ))

    @staticmethod
    def get_filtered_aggregated_statistics(period, start_date):
        """Get aggregated statistics for a certain period"""
        start = PeriodCalculator.calculate_start_date(period) if start_date is None else DateTimeParser.parse(start_date)
        end = PeriodCalculator.calculate_end_date(start, period)
        stats = StatisticService.get_aggregated_statistics(PeriodCalculator.calculate_interval(period),start,end)

        return list(filter(lambda s: end >= s["timestamp"] >= start , stats))

    @staticmethod
    def get_statistics_summary(period):
        """Calculates an end date based on a start date and period"""

        current = PeriodCalculator.calculate_start_date(period)
        previous = PeriodCalculator.calculate_end_date(current,period,True)
        stats = StatisticService.get_aggregated_statistics(period)
        
        cur_stats = list(filter(lambda s: s["timestamp"] == current, stats))
        prev_stats = list(filter(lambda s: s["timestamp"] == previous, stats))
        min_stats = list(sorted(stats, key=lambda s: s["total_usage"]))
        max_stats = list(sorted(stats, key=lambda s: s["total_usage"], reverse=True))
        avg_stats = reduce(lambda x,s: x + s, (s["total_usage"] for s in stats)) if len(stats) > 0 else 0
        
        return {
            'current' : cur_stats[0] if len(cur_stats) > 0 else {"usage" : 0},
            'previous': prev_stats[0] if len(prev_stats) > 0 else {"usage" : 0},
            'min': min_stats[0] if len(min_stats) > 0 else {"usage" : 0},
            'max': max_stats[0] if len(max_stats) > 0 else {"usage" : 0},
            'avg' : avg_stats / len(stats) if len(stats) > 0 else {"usage" : 0}
        }
    

