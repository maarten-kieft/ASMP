from updater.containers.dockerimage import DockerImage

class DockerContainer:
    """A docker component which run individually"""
    container = None
    docker_image = None

    def __init__(self, container):
        self.container = container
        self.docker_image = DockerImage(container.image)

    def start(self):
        """Starting a new container for the given image"""
        self.container.start()

    def stop(self):
        """Stopping al running containers for the given image"""
        self.container.stop()

    def get_id(self):
        return self.container.id

    def get_name(self):
        """Getting the name of the container"""
        return self.docker_image.get_name()

    def get_version(self):
        """Getting the version of the container"""
        return self.docker_image.get_version()

    def get_architecture(self):
        """Getting the architecture of the container"""
        return self.docker_image.get_architecture()

    def cleanup(self):
        self.container.stop()
        self.container.remove()