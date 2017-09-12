from django.test import TestCase
from collections import namedtuple
from updater.updater import Updater
from updater.dockercomponent import DockerComponent
from updater.dockerimagenameparser import DockerImageNameParser

class UpdaterTestCase(TestCase):
    #def setUp(self):
        #Animal.objects.create(name="lion", sound="roar")
        #Animal.objects.create(name="cat", sound="meow")

    def test_compose_valid_image_name(self):
        """Animals that can speak are correctly identified"""
        
        Container = namedtuple('FakeDockerContainer', 'image')
        Image = namedtuple('FakeDockerImage', 'tags')
        updater = Updater()
        updater.updater = DockerComponent();
        updater.updater.container = Container(Image(["blackhawkdesign/asmp-updater-linarm:latest"]))

        image_name = updater.compose_image_name("processor")
        
        self.assertEqual(image_name, "blackhawkdesign/asmp-processor-linarm")

    def test_parse_image_name(self):
        result = DockerImageNameParser.get_short_image_name("blackhawkdesign/asmp-processor-lin64:latest")

        self.assertEqual(result, "blackhawkdesign/asmp-processor-lin64")