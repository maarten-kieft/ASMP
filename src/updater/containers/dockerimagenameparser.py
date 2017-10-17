import re

class DockerImageNameParser:
    """Parses the name of the docker image into parts"""
    @staticmethod
    def parse(image_name):
        """Parses the full image name into blocks"""
        return re.search('blackhawkdesign\/asmp-([^-]+)-([^:]+):?(.*)', image_name)

    @staticmethod
    def get_architecture(image_name):
        """Get the architecture in the image name"""
        result = DockerImageNameParser.parse(image_name)

        return result if result is None else result.group(2) 

    @staticmethod
    def get_component(image_name):
        """Get the component in the image name"""
        result = DockerImageNameParser.parse(image_name)

        return result if result is None else result.group(1) 

    @staticmethod
    def get_version(image_name):
        """Get the version in the image name"""
        result = DockerImageNameParser.parse(image_name)

        return result if result is None else result.group(3) 
    
    @staticmethod
    def get_short_image_name(image_name):
        """Get the image name without version"""

        result = DockerImageNameParser.parse(image_name)
    
        return "blackhawkdesign/asmp-"+ result.group(1) +"-"+result.group(2)