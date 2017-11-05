from django.test import TestCase
from unittest.mock import MagicMock, PropertyMock, patch
from docker.client import DockerClient
from docker.models.containers import Container, ContainerCollection
from updater.containers.dockercomponentfactory import DockerComponentFactory
import docker

class MyClass:
    @property
    def last_transaction(self):
        # an expensive and complicated DB query here
        return "hello!"

    def simpleMethod(self):
        return "hi!"

class DockerComponentFactoryTestCase(TestCase):
    def test_lasttry(self):
        mock = MagicMock()

        with patch.object(MyClass, 'last_transaction', new_callable=PropertyMock) as mock_labels:
            mock_labels.return_value = "goodby"

            instance = MyClass()
            print(instance.last_transaction)

    def test_resolve_component_by_details(self):
        """Test if get name returns the correct name"""
        mock = MagicMock()

        with patch.object(docker.models.containers.Container,'labels', new_callable=PropertyMock) as mock_labels:
            mock_labels.return_value = {
                "component" : "test-component",
                "environment": "lin64",
                "version": "1.0"
            }

            container = Container()

            with patch.object(docker.models.containers.ContainerCollection,'list',return_value=[container]) as mock_container_collection:
                collection = ContainerCollection()
                result = collection.list()
                import pdb;pdb.set_trace()
                a = ""
            #
            #     with mock.patch('DockerClient.containers', new_callable=PropertyMock) as mock_client:
            #         mock_client.return_value = collection
            #         client = DockerClient()
            #
            #         factory = DockerComponentFactory(client)
            #         result = factory.resolve_component_by_details("test-component","lin64","1.0")
            #         self.assertEqual(result.get_name() , "test-component")
