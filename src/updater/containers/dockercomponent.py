import docker

from core.services.messageservice import MessageService
from updater.containers.dockerimagenameparser import DockerImageNameParser


class DockerComponent:
    """A docker component which run individually"""
    client = docker.from_env()
    container = None

    def __init__(self, container):
        self.container = container

    def start(self):
        """Starting a new container for the given image"""
        self.container.start()

    def stop(self):
        """Stopping al running containers for the given image"""
        self.container.stop()

    def get_version(self):
        """Getting the version of the container"""
        for key, value in self.container.image.labels:
            if key == ""
            if result is not None and result is not "latest":
                return result
    
    def get_architecture(self):
        """Getting the architecture of the container"""
        for tag in self.container.image.tags:
            result = DockerImageNameParser.get_architecture(tag)
            
            if result is not None:
                return result
    