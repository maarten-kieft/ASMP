import os
import time
from core.services.messageservice import MessageService
from updater.dockercomponent import DockerComponent

class Updater:
    """Class responsible for updating the whole docker container"""
    
    running = False
    data_volume = None
   
    def start(self):
        """Stats the updater"""
        if not self.valid_update_container():
            MessageService.log_error("updater","Stopping, container not started with the right parameters")
            return

        self.init_components()

        while True:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60 * 60)

            if self.requires_update():
                self.updater.pull()
                self.updater.start()
                return

    def valid_update_container(self):
        """Validates if this containers is started with the right parameters"""
        return True

    def init_components(self):
        updater_container_id = os.environ['HOSTNAME']
        self.updater = DockerComponent(image_name = "blackhawkdesign/asmp-updater-lin64", container_id = updater_container_id)
        self.web = DockerComponent(image_name = "blackhawkdesign/asmp-web-lin64", ports={81:81},volumes_from=[updater_container_id])
        self.processor = DockerComponent(image_name = "blackhawkdesign/asmp-processor-lin64",volumes_from=[updater_container_id])
        self.aggregator = DockerComponent(image_name = "blackhawkdesign/asmp-aggregator-lin64",volumes_from=[updater_container_id])
        
        self.updater.stop()
        self.updater.cleanup()
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