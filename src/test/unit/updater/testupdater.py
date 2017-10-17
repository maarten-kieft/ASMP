from collections import namedtuple

from django.test import TestCase
from updater.dockercomponent import DockerComponent

from updater.containers.dockerimagenameparser import DockerImageNameParser
from updater.updater import Updater


class UpdaterTestCase(TestCase):
    #def setUp(self):
        #Animal.objects.create(name="lion", sound="roar")
        #Animal.objects.create(name="cat", sound="meow")

    def generate_updater(self):
        Container = namedtuple('FakeDockerContainer', 'image')
        Image = namedtuple('FakeDockerImage', 'tags')
        updater = Updater()
        updater.updater = DockerComponent();
        updater.updater.container = Container(Image(["blackhawkdesign/asmp-updater-linarm:latest"]))

        return updater

    def test_compose_valid_image_name(self):
        """Test if composing a image returns a valid image name"""
        updater = self.generate_updater()
        image_name = updater.compose_image_name("processor")
        
        self.assertEqual(image_name, "blackhawkdesign/asmp-processor-linarm")

    def test_valid_requires_update_check_output(self):
        """Test if the requires update check returns valid data"""
        updater = self.generate_updater()
        update_check_result = updater.requires_update()
        
        self.assertEqual(update_check_result["update"], False)

    def test_parse_image_name(self):
        result = DockerImageNameParser.get_short_image_name("blackhawkdesign/asmp-processor-lin64:latest")

        self.assertEqual(result, "blackhawkdesign/asmp-processor-lin64")