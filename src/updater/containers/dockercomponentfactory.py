from updater.containers.dockercomponent import DockerComponent

class DockerComponentFactory:
    """Factory class to generate docker component"""

    def __init__(self, client):
        self.client= client

    def resolve_component_by_details(self, name,architecture, version):
        """Picks already running container or creates a new one"""
        containers = self.client.containers.list(all=True)

        for container in containers:
            component = DockerComponent(container)

            if(component.get_name() == name and component.get_architecture() == architecture and component.get_version() == version):
                return component

        return self.create_component(name,architecture,version)

    def resolve_component_by_id(id):
        """Picks already running container or creates a new one"""
        raise Exception("implement")
        #loop through all images
        #if is the same component as I want, check version, if the same just pick it.
        #pull new images
        #create new container
        #pass it to component


    def create_component(self,name,architecture,version):
        raise Exception("implement")

        self.client.images.pull(self.image_name, version)
        #pull new images
        #create new container
        #pass it to component




#     def pull(self, version = None):
#         """Pulling a new version of the image"""
#         if version is None:
#             version = self.version
#
#         MessageService.log_info("updater", "Pulling image: " + self.image_name + ", version: " + version)
#         self.client.images.pull(self.image_name, version)
# #self.container = self.container.run(self.image_name, None, detach=True, **self.startup_parameters)
#
#     def cleanup(self):
#         """Removing old stopped containers for the given image"""
#         MessageService.log_info("updater", "Cleaning up: " + self.image_name)
#
#         for container in self.client.containers.list(filters={"status": "exited"}):
#             if len(container.image.tags) > 0 and self.image_name in container.image.tags[0]:
#                 container.remove()
#
#     def get_image_name(self):
#         """Getting the image name by the property or by the container"""
#         if self.image_name is not None:
#             return self.image_name
#
#         for tag in self.container.image.tags:
#             result = DockerImageNameParser.get_short_image_name(tag)
#
#             if result is not None:
#                 return result
#
#         return None
#
