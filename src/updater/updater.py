import os
import time
import http.client 
from core.services.messageservice import MessageService
from core.services.applicationservice import ApplicationService
from updater.dockercomponent import DockerComponent

class Updater:
    """Class responsible for updating the whole docker container"""

    updater = None
    web = None
    processor = None
    aggregator = None

    def start(self):
        """Stats the updater"""
        MessageService.log_info("updater","Starting..")
        if not self.valid_update_container():
            MessageService.log_error("updater","Stopping, container not started with the right parameters")
            return

        self.init_components()

        while True:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60)

            if self.requires_update():
                self.updater.pull()
                self.updater.start()
                return

    def valid_update_container(self):
        """Validates if this containers is started with the right parameters"""
        return True

    def init_components(self):
        """Init the docker components"""
        MessageService.log_error("updater","Init components")
        updater_container_id = os.environ['HOSTNAME']
        self.updater = DockerComponent(container_id = updater_container_id)
        self.web = DockerComponent(image_name = self.compose_image_name("web"), ports={81:81},volumes_from=[updater_container_id])
        self.processor = DockerComponent(image_name = self.compose_image_name("processor"),volumes_from=[updater_container_id], privileged=True)
        self.aggregator = DockerComponent(image_name = self.compose_image_name("aggregator"),volumes_from=[updater_container_id])
        
        self.updater.stop()
        self.updater.cleanup()
        self.web.init()
        self.processor.init()
        self.aggregator.init()
        MessageService.log_info("updater","Initialized components")

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        application_id = ApplicationService.application_id()
        version = self.updater.get_version()

        conn = http.client.HTTPConnection("www.kieft.ws")
        conn.request("GET","/asmp/update-check.php?application_id="+application_id+"&version="+version)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        return  data == "true"

    def compose_image_name(self, component_name):
        """Compose the image name of a docker component"""
        architecture = self.updater.get_architecture()

        return "blackhawkdesign/asmp-" + component_name + "-" + architecture