import time
from core.services.messageservice import MessageService
from updater.dockercomponent import DockerComponent

class Updater:
    """Class responsible for updating the whole docker container"""
    running = True

    def __init__(self):
        self.updater = DockerComponent("blackhawkdesign/asmp-updater-lin64")
        self.processor = DockerComponent("blackhawkdesign/asmp-processor-lin64")
        self.aggregator = DockerComponent("blackhawkdesign/asmp-aggregator-lin64")
        self.web = DockerComponent("blackhawkdesign/asmp-web-lin64", ports={81:81})

    def start(self):
        """Stats the updater"""
        #self.processor.init()
        #self.aggregator.init()
        self.web.init()
        MessageService.log_info("updater","Initialized components")

        while self.running:
            MessageService.log_info("updater","Sleeping for 60 minutes for the next update check")
            time.sleep(60 * 60)

            if self.requires_update():
                self.updater.init()
                self.running = False

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        return True