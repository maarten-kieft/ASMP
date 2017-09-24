from django.test import TestCase
from collections import namedtuple
from updater.updater import Updater
from updater.dockercomponent import DockerComponent
from updater.dockerimagenameparser import DockerImageNameParser

class AggregatorTestCase(TestCase):

    def test_cleanup(self):
        """Test if cleanup works properly"""
     
        
        #self.assertEqual("a", "b")
