from django.test import TestCase
from collections import namedtuple
from aggregator.aggregator import Aggregator

class AggregatorTestCase(TestCase):

    def test_cleanup(self):
        """Test if cleanup works properly"""
     
        ag = Aggregator()
        ag.cleanup_measurements()
        #self.assertEqual("a", "")
