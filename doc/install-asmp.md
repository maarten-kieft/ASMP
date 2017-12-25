

1. Create a data directoryt for asmp
  `mkdir /usr/bin/asmp/data`

* Start asmp
  `docker run -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-updater-linarm:latest`
  
* Open a brower and navigate to
  `localhost`