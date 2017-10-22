@echo off
set /p version="Enter version: "

docker build -t blackhawkdesign/asmp-web-linarm:latest -f docker/linarm/Dockerfile-web-linarm --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-processor-linarm:latest -f docker/linarm/Dockerfile-processor-linarm --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-aggregator-linarm:latest -f docker/linarm/Dockerfile-aggregator-linarm --build-arg VERSION=%version% .
docker build -t blackhawkdesign/asmp-updater-linarm:latest -f docker/linarm/Dockerfile-updater-linarm --build-arg VERSION=%version% .

docker push blackhawkdesign/asmp-web-linarm:%version%
docker push blackhawkdesign/asmp-processor-linarm:%version%
docker push blackhawkdesign/asmp-aggregator-linarm:%version%
docker push blackhawkdesign/asmp-updater-linarm:%version%

docker push blackhawkdesign/asmp-web-linarm:latest
docker push blackhawkdesign/asmp-processor-linarm:latest
docker push blackhawkdesign/asmp-aggregator-linarm:latest
docker push blackhawkdesign/asmp-updater-linarm:latest