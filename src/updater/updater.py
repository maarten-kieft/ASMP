import time
from core.services.messageservice import MessageService
from dockercomponent import DockerComponent

class Updater:
    """Class responsible for updating the whole docker container"""
    running = True

    def __init__(self):
        command = "start.sh"
        self.updater = DockerComponent("blackhawkdesign/asmp-updater-x64", command, [])
        self.processor = DockerComponent("blackhawkdesign/asmp-processor-x64", command, [])
        self.aggregator = DockerComponent("blackhawkdesign/asmp-aggregator-x64", command, [])
        self.web = DockerComponent("blackhawkdesign/asmp-web-x64", command, [])

    def start(self):
        """Stats the updater"""
        self.processor.init()
        self.aggregator.init()
        self.web.init()

        while self.running:
            time.sleep(60 * 60)

            if self.requires_update():
                self.updater.init()
                self.running = False

    def requires_update(self):
        """"Checks if an update is required"""
        MessageService.log_info("updater","Checking for updates")
        return True