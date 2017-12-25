from datetime import datetime, timedelta
from core.services.statisticservice import StatisticService
from core.models import Statistic, Meter
from unittest import TestCase
import pytz

class StatisticServiceTestCase(TestCase):
    def setUp(self):
        Statistic.objects.all().delete()
        Meter.objects.all().delete()

    def test_create_statistics(self):
        meter = Meter.objects.get_or_create(name="integrationtest-meter")[0]

        aggregated_measurements = [
            {
                "meter_id" : meter.id,
                "timestamp_start" :datetime.now(pytz.utc).replace(tzinfo=pytz.utc),
                "power_usage_start" : 500,
                "power_usage_end" : 1000,
                "power_supply_start" : 400,
                "power_supply_end": 800
            }
        ]

        StatisticService.create_statistics(aggregated_measurements)
        statistics = Statistic.objects.all()
        self.assertEqual(1,len(statistics))
        self.assertEqual(500,statistics[0].power_usage_start)
        self.assertEqual(1000,statistics[0].power_usage_end)
        self.assertEqual(400,statistics[0].power_supply_start)
        self.assertEqual(800,statistics[0].power_supply_end)

