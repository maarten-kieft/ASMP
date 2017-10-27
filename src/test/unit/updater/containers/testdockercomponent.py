from collections import namedtuple
from django.test import TestCase
from updater.containers.dockercomponent import DockerComponent

class DockerComponentTestCase(TestCase):
    component = None

    def setUp(self):
        container_tuple = namedtuple('FakeDockerContainer', 'image')
        image_tuple = namedtuple('FakeDockerImage', 'labels')
        labels = {
            "component": "test-component",
            "environment": "testenvr",
            "version": "1.0"
        }

        self.component = DockerComponent(container_tuple(image_tuple(labels)))

    def test_get_name(self):
        """Test if get name returns the correct name"""
        self.assertEqual(self.component.get_name() , "test-component")

    def test_get_architecture(self):
        """Test if get architecture returns the correct value"""
        self.assertEqual(self.component.get_architecture() , "testenvr")

    def test_get_version(self):
        """Test if get vesion returns the correct value"""
        self.assertEqual(self.component.get_version() , "1.0")
