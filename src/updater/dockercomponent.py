import docker
from core.services.messageservice import MessageService
from updater.dockerimagenameparser import DockerImageNameParser

class DockerComponent:
    """A docker component which run individually"""
    client = docker.from_env()
    container_id = None
    container = None

    def __init__(self, image_name = None, container_id=None, **startup_parameters):
        self.image_name = image_name
        self.container_id = container_id
        self.startup_parameters = startup_parameters

        if self.container_id is not None:
            self.container = self.client.containers.get(container_id)

        if self.container is not None and self.image_name is None:
            self.image_name = self.get_image_name()

    def init(self):
        """Initializes the component by pulling newest version stopping old containers and starting a new one"""
        self.pull()
        self.stop()
        self.start()
        self.cleanup()

    def pull(self):
        """Pulling a new version of the image"""
        MessageService.log_info("updater", "Pulling latest image: " + self.image_name)
        self.client.images.pull(self.image_name, "latest")

    def start(self):
        """Starting a new container for the given image"""
        MessageService.log_info("updater", "Starting new container: " + self.image_name)
        self.container = self.client.containers.run(self.image_name, None, detach=True, **self.startup_parameters)
        self.container_id = self.container.id

    def stop(self):
        """Stopping al running containers for the given image"""
        MessageService.log_info("updater", "Stopping running container: " + self.image_name)

        for container in self.client.containers.list(filters={"status":"running"}):
            if len(container.image.tags) > 0 and self.image_name in container.image.tags[0] and (self.container_id is None or self.container_id not in container.id):
                container.stop()

    def cleanup(self):
        """Removing old stopped containers for the given image"""
        MessageService.log_info("updater", "Cleaning up: " + self.image_name)

        for container in self.client.containers.list(filters={"status":"exited"}):
            if len(container.image.tags) > 0 and self.image_name in container.image.tags[0]:
                container.remove()

    def get_image_name(self):
        """Getting the image name by the property or by the container"""
        if self.image_name is not None:
            return self.image_name

        for tag in self.container.image.tags:
            result = DockerImageNameParser.get_short_image_name(tag)
            
            if result is not None:
                return result
    
        return None

    def get_version(self):
        """Getting the version of the container"""
        if self.container is None:
            return None

        for tag in self.container.image.tags:
            result = DockerImageNameParser.get_version(tag)
            
            if result is not None and result is not "latest":
                return result
    
    def get_architecture(self):
        """Getting the architecture of the container"""
        for tag in self.container.image.tags:
            result = DockerImageNameParser.get_architecture(tag)
            
            if result is not None:
                return result
    