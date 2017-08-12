from subprocess import call
from asmp.services.messageservice import MessageService
class DockerService:
    """Service to perform actions around docker"""

    @staticmethod
    def pull_latest():
        """Logs a info message into the database"""
        call(["docker", "pull", "blackhawkdesign/asmp-x64:latest"])

    @staticmethod
    def start_container(name):
        """Starts a new asmp container in the given mode"""
        MessageService.log_info("dockerservice", "ik ga starten:" + name)
        if name == "asmp-updater":
            call(["docker", "run", "--name", name, "-d", "-v", "/var/run/docker.sock:/var/run/docker.sock", "blackhawkdesign/asmp-x64:latest", "/usr/bin/asmp/update.sh"])
        else:
            call(["docker", "run", "--name", name, "-d", "-v", "/var/run/docker.sock:/var/run/docker.sock", "-p", "81:81", "blackhawkdesign/asmp-x64:latest"])

    @staticmethod
    def stop_container(name):
        """Stops a container"""
        call(["docker", "stop", name])
    
    @staticmethod
    def remove_container(name):
        """Removes a container"""
        call(["docker", "rm", name])
