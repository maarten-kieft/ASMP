# ASMP
Another Smart Meter Project, which allows users to read the values of their (dutch) smart meter, aggregate them and display them in nice graphs. This project is build in python and uses docker to deploy the application. This is work in progress.. 

## Todo

1. Fix static files in docker image V
2. Implement database updates V
3. Implement general way to retrieve updates V
4. Implement statistics V
5. Implement dropdown statistics
6. Implement graph 
7. Implement dropdown graph
8. Merge start files into a single file V
9. Create screenshots
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
