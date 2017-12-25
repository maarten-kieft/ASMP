from collections import namedtuple
from aggregator.aggregator import Aggregator
from unittest import TestCase

class AggregatorTestCase(TestCase):

    def test_cleanup(self):
        """Test if cleanup works properly"""
     
        ag = Aggregator()
        ag.cleanup_measurements()
        #self.assertEqual("a", "")
