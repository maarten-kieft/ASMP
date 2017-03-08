# ASMP
Another Smart Meter Project, which allows users to read the values of their (dutch) smart meter, aggregate them and display them in nice graphs. This project is build in python and uses docker to deploy the application. This is work in progress.. 

## Todo

1. Fix static files in docker image
2. Implement general way to retrieve updates
3. Implement statistics
4. Implement dropdown statistics
5. Implement graph
6. Implement dropdown graph
7. Merge docker files into a single file
8. Merge start files into a single file
9. Create screenshots
10. Create docs for getting started on a pie
11. Create docs for getting started on source


## Commands

Building a new image
```
docker build -t blackhawkdesign/asmp-rpi -f Dockerfile.arm .
```
Tagging the new image
```
docker tag xxx blackhawkdesign/asmp-rpi:latest
```
Pushing the new image
```
docker push blackhawkdesign/asmp-rpi
```
Running an image
```
docker run -p 8000:8000 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-rpi:latest
```
```
docker run -p 8000:8000 
```
Running with bash
```
docker run -t -i mysnapshot /bin/bash
```