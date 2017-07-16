# ASMP
Another Smart Meter Project, which allows users to read the values of their (dutch) smart meter, aggregate them and display them in nice graphs. This project is build in python and uses docker to deploy the application. This is work in progress.. 

## Todo
6. Showing only recent measurements in recent chart / current chart. So only last 5 mins. Otherwise gray out
6. Create screenshots
8. Create docs for getting started on a pie
9. Create docs for getting started on source
10. Showing (health)notifications about the status of processor / aggregator
11. Creating a heartbeat local and remote
12. Implement return charts
13. Implement gas database changes
14. Implement gas ui changes
15. Create update mechanism
## Commands

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
docker run -p 81:81 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-x64:latest
```
```
docker run -p 8000:8000 
```
Running with bash
```
docker run -t -i {containerid} /bin/bash
```
