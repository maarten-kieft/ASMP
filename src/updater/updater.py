import time
from asmp.services.messageservice import MessageService
from asmp.services.dockerservice import DockerService

class Updater:
    """Class responsible for updating the whole docker container"""
    running = True

    def start(self):   
          while self.running:
            MessageService.log_info("updater","Sleeping 1 minute")
            time.sleep(20)

            if self.requires_update():
                self.init_update()

    def requires_update(self):        
        MessageService.log_info("updater","Checking for updates")
        return True

    def init_update(self):
        MessageService.log_info("updater","Init update process")
        DockerService.remove_container("asmp-updater")
        DockerService.start_container("asmp-updater")

    def execute_update(self):
        MessageService.log_info("updater","Pulling latest image")
        DockerService.pull_latest()

        MessageService.log_info("updater","Starting new container")
        DockerService.stop_container("asmp")
        DockerService.remove_container("asmp")
        
        DockerService.start_container("asmp")        
        MessageService.log_info("updater","Exit this container")
