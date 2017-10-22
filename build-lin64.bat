@echo off
set /p version="Enter version: "

docker build -t blackhawkdesign/asmp-web-lin64:latest -f docker/lin64/Dockerfile-web-lin64 --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-processor-lin64:latest -f docker/lin64/Dockerfile-processor-lin64 --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-aggregator-lin64:latest -f docker/lin64/Dockerfile-aggregator-lin64 --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-updater-lin64:latest -f docker/lin64/Dockerfile-updater-lin64 --build-arg VERSION=%version% .

docker push blackhawkdesign/asmp-web-lin64:latest
docker push blackhawkdesign/asmp-processor-lin64:latest
docker push blackhawkdesign/asmp-aggregator-lin64:latest
docker push blackhawkdesign/asmp-updater-lin64:latest