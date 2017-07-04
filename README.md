# ASMP
Another Smart Meter Project, which allows users to read the values of their (dutch) smart meter, aggregate them and display them in nice graphs. This project is build in python and uses docker to deploy the application. This is work in progress.. 

## Todo
5. Implement month/year statistics
6. Implement switching and zoom out in overview chart
8. Bugfix: 30 april 2017 doesnt work: error
10. Loader when click on overview chart
10. One big loader
9. Create screenshots
10. Show health notifications
10. Create docs for getting started on a pie
11. Create docs for getting started on source


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
