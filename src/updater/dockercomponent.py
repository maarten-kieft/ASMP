import docker
from core.services.messageservice import MessageService

class DockerComponent:
    """A docker component which run individually"""
    client = docker.from_env()
    container = None

    def __init__(self, image_name, **startup_parameters):
        self.image_name = image_name
        self.startup_parameters = startup_parameters

    def init(self):
        """Initializes the component by pulling newest version stopping old containers and starting a new one"""
        self.pull()
        self.stop()
        self.start()
        self.cleanup()

    def pull(self):
        """Pulling a new version of the image"""
        MessageService.log_info("updater", "Pulling latest image: " + self.image_name)
        self.client.images.pull(self.image_name,"latest")

    def start(self):
        """Starting a new container for the given image"""
        MessageService.log_info("updater", "Starting new container: " + self.image_name)
        self.container = self.client.containers.run(self.image_name,None,detach=True, **self.startup_parameters)
        
    def stop(self):
        """Stopping al running containers for the given image"""
        MessageService.log_info("updater", "Stopping running container: " + self.image_name)
        
        for container in self.client.containers.list(filters={"status":"running"}):
            if self.image_name in container.image.tags[0]:
                container.stop()

    def cleanup(self):
        """Removing old stopped containers for the given image"""
        MessageService.log_info("updater", "Cleaning up: " + self.image_name)
        
        for container in self.client.containers.list(filters={"status":"exited"}):
            if len(container.image.tags) > 0 and self.image_name in container.image.tags[0]:
                container.remove()