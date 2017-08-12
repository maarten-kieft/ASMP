from subprocess import call

class DockerService:
    """Service to perform actions around docker"""

    @staticmethod
    def pull_latest():
        """Logs a info message into the database"""
        call(["docker", "pull", "blackhawkdesign/asmp-x64:latest"])

    @staticmethod
    def start_container(name):
        """Starts a new asmp container in the given mode"""
        if name == "asmp-updater":
            call(["docker", "run", "-d", "-v", "/var/run/docker.sock:/var/run/docker.sock", "blackhawkdesign/asmp-x64:latest", "/usr/bin/asmp/update.sh"])
        else:
            call(["docker", "run", "--name", name, "-d", "-p", "81:81",  "-v","/var/run/docker.sock:/var/run/docker.sock", "blackhawkdesign/asmp-x64:latest" ])

    @staticmethod
    def stop_container(name):
        """Starts a  container"""
        call(["docker", "stop", name])
        call(["docker", "rm", name])
