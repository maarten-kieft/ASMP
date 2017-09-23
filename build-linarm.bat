@echo off
set /p version="Enter version: "

docker build -t blackhawkdesign/asmp-web-linarm:latest -t blackhawkdesign/asmp-web-linarm:%version% -f docker/linarm/Dockerfile-web-linarm .
docker build -t blackhawkdesign/asmp-processor-linarm:latest -t blackhawkdesign/asmp-processor-linarm:%version% -f docker/linarm/Dockerfile-processor-linarm .
docker build -t blackhawkdesign/asmp-aggregator-linarm:latest -t blackhawkdesign/asmp-aggregator-linarm:%version% -f docker/linarm/Dockerfile-aggregator-linarm .
docker build -t blackhawkdesign/asmp-updater-linarm:latest -t blackhawkdesign/asmp-updater-linarm:%version% -f docker/linarm/Dockerfile-updater-linarm .

docker push blackhawkdesign/asmp-web-linarm:%version%
docker push blackhawkdesign/asmp-processor-linarm:%version%
docker push blackhawkdesign/asmp-aggregator-linarm:%version%
docker push blackhawkdesign/asmp-updater-linarm:%version%

docker push blackhawkdesign/asmp-web-linarm:latest
docker push blackhawkdesign/asmp-processor-linarm:latest
docker push blackhawkdesign/asmp-aggregator-linarm:latest
docker push blackhawkdesign/asmp-updater-linarm:latest