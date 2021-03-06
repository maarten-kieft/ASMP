from collections import namedtuple
from unittest import TestCase
from updater.containers.dockercontainer import DockerContainer
from docker.models.containers import Container
from unittest.mock import MagicMock, PropertyMock, patch
import docker

class DockerContainerTestCase(TestCase):

    def test_get_name(self):
        """Test if get name returns the correct name"""
        with patch.object(Container, 'image', new_callable=PropertyMock) as mock:
            type(mock.return_value).labels = PropertyMock(return_value={"component": "test-component"})

            self.assertEqual(DockerContainer(Container()).get_name() , "test-component")

    def test_get_architecture(self):
        """Test if get architecture returns the correct value"""
        with patch.object(Container, 'image', new_callable=PropertyMock) as mock:
            type(mock.return_value).labels = PropertyMock(return_value={"environment": "lin64"})

            self.assertEqual(DockerContainer(Container()).get_architecture() , "lin64")


    def test_get_version(self):
        """Test if get vesion returns the correct value"""
        with patch.object(Container, 'image', new_callable=PropertyMock) as mock:
            type(mock.return_value).labels = PropertyMock(return_value={"version": "1.1"})

            self.assertEqual(DockerContainer(Container()).get_version() , "1.1")
