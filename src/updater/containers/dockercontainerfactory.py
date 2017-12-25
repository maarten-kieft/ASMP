from updater.containers.dockercontainer import DockerContainer
from updater.containers.dockerimage import DockerImage

class DockerContainerFactory:
    """Factory class to generate docker component"""
    client = None
    updater_component = None

    def __init__(self, client,updater_container_id):
        self.client= client
        self.updater_component = self.resolve_component_by_id(updater_container_id)

    def resolve_component_by_id(self, id):
        container = self.get_containers(id)

        if container is None:
            return None

        return DockerContainer(container)

    def resolve_component_by_details(self, name, version = None):
        """Picks already running container or creates a new one"""
        architecture = self.updater_component.get_architecture()

        if version is None:
            version = self.updater_component.get_version()

        for container in self.get_containers():
            component = DockerContainer(container)

            if(component.get_name() == name and component.get_architecture() == architecture and component.get_version() == version):
                return component

        return self.create_component(name,architecture,version)

    def create_component(self,name,architecture,version):
        image_name = "blackhawkdesign/asmp-{0}-{1}:{2}".format(name,architecture,version)
        startup_parameters = self.compose_startup_parameters(name)
        self.client.images.pull(image_name)

        container = self.client.containers.create(image = image_name,detach=True,**startup_parameters)
        component = DockerContainer(container)

        return component

    def get_containers(self, id = None):
        if self.client is None:
            return None

        if id is None:
            return self.client.containers.list(all=True)

        return self.client.containers.get(id)

    def get_images(self):
        return self.client.images.list()

    def compose_startup_parameters(self, name):
        args = {"volumes_from" : [self.updater_component.get_id()]}

        if name == "processor":
            args["privileged"] = True

        if name == "web":
            args["ports"] = {80: 80}

        return args

    def cleanup_containers(self, name):
        """Picks already running container or creates a new one"""
        architecture = self.updater_component.get_architecture()
        version = self.updater_component.get_version()

        for container in self.get_containers():
            dockerComponent = DockerContainer(container)

            if (dockerComponent.get_name() == name and (dockerComponent.get_architecture() != architecture or dockerComponent.get_version() != version)):
                dockerComponent.cleanup()

    def cleanup_images(self,name):
        architecture = self.updater_component.get_architecture()
        version = self.updater_component.get_version()

        for image in self.get_images():
            dockerImage = DockerImage(image)

            if (dockerImage.get_name() == name and (dockerImage.get_architecture() != architecture or dockerImage.get_version() != version)):
                self.client.images.remove(image=image.id,force=True)
