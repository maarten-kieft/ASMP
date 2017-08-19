import time
import docker
import os
from core.services.messageservice import MessageService
from updater.dockercomponent import DockerComponent
from core.services.messageservice import MessageService

class Updater:
    """Class responsible for updating the whole docker container"""
    
    running = False
    data_volume = None

    def __init__(self): 
        self.client = docker.from_env()
        self.updater_container = self.client.containers.get(os.environ['HOSTNAME'])
           
    def start(self):
        """Stats the updater"""
        if not self.valid_update_container():
            MessageService.log_error("updater","Stopping, container not started with the right parameters")
            return

        self.init_components()
        self.running = True
        
        while self.running:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60 * 60)

            if self.requires_update():
                self.running = False

    def valid_update_container(self):
        """Validates if this containers is started with the right parameters"""
        return True

    def init_components(self):
        #self.updater = DockerComponent("blackhawkdesign/asmp-updater-lin64",volumes_from=[self.updater_container.id])
        self.web = DockerComponent("blackhawkdesign/asmp-web-lin64", ports={81:81},volumes_from=[self.updater_container.id])
        self.processor = DockerComponent("blackhawkdesign/asmp-processor-lin64",volumes_from=[self.updater_container.id])
        self.aggregator = DockerComponent("blackhawkdesign/asmp-aggregator-lin64",volumes_from=[self.updater_container.id])
        
        self.web.init()
        self.processor.init()
        self.aggregator.init()
        MessageService.log_info("updater","Initialized components")

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        return True

    def get_current_container(self):
         for container in self.client.containers.list(filters={"status":"running"}):
            if "blackhawkdesign/asmp-updater" in container.image.tags[0]:
                return container