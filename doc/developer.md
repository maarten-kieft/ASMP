## Commands

Todo
1. Gebruik juiste platform (lin 64 / arm)
2. poort voor web door geven




Building a new image
```
docker build -t blackhawkdesign/asmp-arm -f Dockerfile.arm .
docker build -t blackhawkdesign/asmp-x64 -f Dockerfile.x64 .
```
Pushing the new image
```
docker push blackhawkdesign/asmp-arm
docker push blackhawkdesign/asmp-x64
```
Pulling the most recent image
```
docker pull blackhawkdesign/asmp-arm:latest
```
Running an image
```
docker run -p 81:81 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-arm:latest
docker run -p 81:81 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data -v /var/run/docker.sock:/var/run/docker.sock  blackhawkdesign/asmp-x64:latest
```
```
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-updater-lin64:latest
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-updater-linarm:latest
```
Running with bash
```
docker run -t -i {containerid} /bin/bash
```