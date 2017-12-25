
class DockerImage:
    """A docker component which run individually"""
    image = None

    def __init__(self, image):
        self.image = image

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
        for key, value in self.image.labels.items():
            if key == label_key:

                return value

        return None