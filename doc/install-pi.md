
Downloads pagina : https://www.raspberrypi.org/downloads/

Ubuntu mate download pagina: https://ubuntu-mate.org/raspberry-pi/
https://ubuntu-mate.org/download/

download https://etcher.io/

download image
download etcher en burn het op de image
sluit shit en image aan in pi, installatie starten
vul taal, timezone in, username en comp name

daarna 
apt-get update
apt-get install ssh

sudo service ssh restart

-----------------------

docker:
https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository


depedencies for adding repo
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

add the repo key ? 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo add-apt-repository "deb [arch=armhf] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update

sudo apt-get install docker-ce

mkdir /usr/bin/asmp/data

sudo docker run -p 81:81 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-arm:latest

sudo mkdir /p /usr/bin/asmp/data