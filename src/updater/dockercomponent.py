import docker

class DockerComponent:
    client = docker.from_env()
    container = None

    def __init__(self, image_name,command, startup_parameters):
        self.image_name = image_name
        self.command = command
        self.startup_parameters = startup_parameters

    def init(self):
        self.pull()
        self.stop()
        self.start()
        self.cleanup()

    def pull(self):
        self.client.images.pull(self.image_name,"latest")

    def start(self):
        self.container = self.client.containers.run(self.image_name,self.command,self.startup_parameters)
        
    def stop(self):
        for container in this.client.containers.list(status=running)
            if image = container.image.tags[0] == self.image_name:
                container.stop()

    def cleanup(self):
        for image in this.client.images.list():
            if image.tags[0] == self.image_name:
                image.remove()
    