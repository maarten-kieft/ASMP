
class DockerContainer:
    """A docker component which run individually"""
    container = None

    def __init__(self, container):
        self.container = container

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
        return self.get_label_value("component")

    def get_version(self):
        """Getting the version of the container"""
        return self.get_label_value("version")

    def get_architecture(self):
        """Getting the architecture of the container"""
        return self.get_label_value("environment")

    def get_label_value(self, label_key):
        """Getting the label value of the container"""
        for key, value in self.container.image.labels.items():
            if key == label_key:

                return value

        return None

    def cleanup(self):
        self.container.stop()
        self.container.remove()