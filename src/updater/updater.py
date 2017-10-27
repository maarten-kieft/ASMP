from core.services.applicationservice import ApplicationService
from core.services.messageservice import MessageService
from updater.containers.dockercomponent import DockerComponent
import http.client
import os
import time
import docker;

class Updater:
    """Class responsible for updating the whole docker container"""

    client = docker.from_env()

    updater = None
    web = None
    processor = None
    aggregator = None

    def start(self):
        """Stats the updater"""
        MessageService.log_info("updater","Starting..")
        if not self.valid_update_container():
            MessageService.log_info("updater","Stopping, container not started with the right parameters")
            return

        self.init_components()

        while True:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60)

            update_result = self.requires_update() 
            if update_result["update"]:
                self.updater.pull(update_result["version"])
                self.updater.start()
                return

    def valid_update_container(self):
        """Validates if this containers is started with the right parameters"""
        return True

    def init_components(self):
        """Init the docker components"""
        MessageService.log_info("updater","Init components")
        updater_container_id = os.environ['HOSTNAME']
        self.updater = DockerComponent(container_id = updater_container_id)
        self.web = DockerComponent(image_name = self.compose_image_name("web"), version = self.resolve_version(), ports={81:81}, volumes_from=[updater_container_id])
        self.processor = DockerComponent(image_name = self.compose_image_name("processor"), version = self.resolve_version(), volumes_from=[updater_container_id], privileged=True)
        self.aggregator = DockerComponent(image_name = self.compose_image_name("aggregator"), version = self.resolve_version() ,volumes_from=[updater_container_id])
        
        self.updater.stop()
        self.updater.cleanup()
        self.web.init()
        self.processor.init()
        self.aggregator.init()
        MessageService.log_info("updater","Initialized components")

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        application_id = ApplicationService.get_id()
        version = self.updater.get_version()

        try:
            conn = http.client.HTTPConnection("www.kieft.ws")
            conn.request("GET","/asmp/update-check.php?application_id="+application_id+"&version="+version)
            res = conn.getresponse()
            data = res.read().decode("utf-8")

            return  { 
                "update" : data != "false", 
                "version" : data if data != "false" else None
            }
        except :
            MessageService.log_error("updater","Unexpected exception:" + sys.exc_info()[0])
        finally:
            conn.close()

    def compose_image_name(self, component_name):
        """Compose the image name of a docker component"""
        architecture = self.updater.get_architecture()

        return "blackhawkdesign/asmp-" + component_name + "-" + architecture

    def resolve_version(self):
        return self.updater.get_version()