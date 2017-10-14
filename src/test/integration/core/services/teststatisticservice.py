from django.test import TestCase
from core.services.statisticservice import StatisticService
from core.models import Statistic

class StatisticServiceTestCase(TestCase):
    def setUp(self):
        Statistic.objects.all().delete()

    def test_get_aggregated_statistics(self):
        statistics = StatisticService.get_filtered_aggregated_statistics("hour",None)
        self.assertEqual(0,len(statistics))