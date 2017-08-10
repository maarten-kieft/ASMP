from subprocess import call
import time
from asmp.services.messageservice import MessageService

class Updater:
    """Class responsible for updating the whole docker container"""
    running = True

    def start(self):
          self.startup_application()
          
          while self.running:
            MessageService.log_info("updater","Sleeping 1 minute")
            time.sleep(30)

            if self.requires_update():
                self.update()
    
    def startup_application(self):
        call(["docker", "pull","blackhawkdesign/asmp-web-x64:latest"])
        call(["docker", "run","-p","81:81","--device=/dev/ttyUSB0","-v","/usr/bin/asmp:/usr/bin/asmp/data", "blackhawkdesign/asmp-x64:latest"])

    def requires_update(self):        
        MessageService.log_info("updater","Checking for updates")
        return True

    def update(self):
        MessageService.log_info("updater","Pulling latest image")
        call(["docker", "pull","blackhawkdesign/asmp-x64:latest"])

        MessageService.log_info("updater","Start new container")
                
        MessageService.log_info("updater","Exit this container")
        self.running = False