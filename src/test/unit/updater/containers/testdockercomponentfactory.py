from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock, patch
from docker.models.containers import Container
from updater.containers.dockercontainerfactory import DockerContainerFactory
from updater.containers.dockercontainer import DockerContainer

class DockerContainerFactoryTestCase(TestCase):
    factory = None

    def setUp(self):
        updater = DockerContainer(None)
        updater.get_version = MagicMock(return_value="1.0")
        updater.get_architecture = MagicMock(return_value="lin64")
        self.factory = DockerContainerFactory(None, None)
        self.factory.updater_component = updater

    def test_resolve_component_by_details_existing(self):
        """Test it can resolve the correct name"""
        with patch.object(Container, 'image', new_callable=PropertyMock) as mock:
            labels = {"component" : "test-component","environment": "lin64","version": "1.0"}
            type(mock.return_value).labels = PropertyMock(return_value=labels)
            self.factory.get_containers = MagicMock(return_value=[Container()])

            component = self.factory.resolve_component_by_details("test-component")
            self.assertEqual(component.get_name(),"test-component")
            self.assertEqual(component.get_architecture(),"lin64")
            self.assertEqual(component.get_version(),"1.0")

    def test_resolve_component_by_details_new(self):
        """Test if get name returns the correct name"""
        self.factory.get_containers = MagicMock(return_value=[])
        self.factory.create_component = MagicMock(return_value=None)
        self.factory.resolve_component_by_details("test-component")
        self.factory.create_component.assert_called_with("test-component","lin64","1.0")
