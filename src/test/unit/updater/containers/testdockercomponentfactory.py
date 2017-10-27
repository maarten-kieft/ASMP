from django.test import TestCase
from unittest.mock import MagicMock, PropertyMock
from docker.client import DockerClient
from docker.models.containers import Container, ContainerCollection
from updater.containers.dockercomponentfactory import DockerComponentFactory
import docker

class DockerComponentFactoryTestCase(TestCase):
    client = None
    factory = None

    def setUp(self):
        self.client = docker.from_env()

    def test_resolve_component_by_details(self):
        """Test if get name returns the correct name"""
        mock = MagicMock()

        with mock.patch(Container,'labels', new_callable=PropertyMock) as mock_container:
            mock_container.return_value = {
                "component" : "test-component",
                "environment": "lin64",
                "version": "1.0"
            }

            container = Container()
            import pdb;
            pdb.set_trace()
            with mock.patch('ContainerCollection.list', new_callable=PropertyMock) as mock_container_collection:
                mock_container_collection.return_value = [container]
                collection = ContainerCollection()

                with mock.patch('DockerClient.containers', new_callable=PropertyMock) as mock_client:
                    mock_client.return_value = collection
                    client = DockerClient()

                    factory = DockerComponentFactory(client)
                    result = factory.resolve_component_by_details("test-component","lin64","1.0")
                    self.assertEqual(result.get_name() , "test-component")
