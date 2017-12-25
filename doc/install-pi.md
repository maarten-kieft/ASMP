# Setup raspberry pi 3
The following guide walk you through the steps to get a raspberry pi up and running for asmp:

## Install ubuntu mate
1. Insert your sd cart into your computer 
* Navigate to https://ubuntu-mate.org/download/ to get a copy of ubuntu mate for raspberry pi 2 or 3
* Download the program etcher https://etcher.io/ to write the image to the sd card
* Install etcher and start it
* In etcher select the ubuntu mate image, select the sd card and click on `Flash!`
* Insert the sd card in the raspberry pi and boot it
* Follow the installation instructions, remember your username and password you need it later

## Install docker
 After installation of ubuntu we can install docker. The instructions are copied from the offical docker docs: https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository
 
* Open a terminal: applications > system tools > MATE terminal
* First update apt package index
  `sudo apt-get update`
* Install the required tools
  `sudo apt-get install apt-transport-https ca-certificates curl software-properties-common`
* Add the GPG key for the official Docker repository to the system:
  `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
* Add the docker repository
  `sudo add-apt-repository "deb [arch=armhf] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
* Update the apt package index with the new repository
  `sudo apt-get update`
* Install docker
  `sudo apt-get install docker-ce`
