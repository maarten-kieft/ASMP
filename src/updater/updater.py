from core.services.applicationservice import ApplicationService
from core.services.messageservice import MessageService
from updater.containers.dockercomponentfactory import DockerComponentFactory
import http.client
import os
import time
import docker;

class Updater:
    """Class responsible for updating the whole docker container"""

    factory = None

    def start(self):
        """Stats the updater"""
        MessageService.log_info("updater","Starting..")
        self.init_components()
        self.run_update_loop()

    def init_components(self):
        """Init the docker components"""
        self.factory = DockerComponentFactory(docker.from_env(),os.environ['HOSTNAME'])

        for name in ["web", "processor", "aggregator"]:
            self.factory.cleanup_component(name)
            component = self.factory.resolve_component_by_details(name)
            component.start()

        MessageService.log_info("updater","Initialized components")

    def run_update_loop(self):
        while True:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60)

            update_result = self.requires_update()
            if update_result["update"]:
                updater_component = self.factory.resolve_component_by_details("updater",update_result["version"])
                updater_component.start()

                return

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        application_id = ApplicationService.get_id()
        version = self.factory.updater_component.get_version()

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
