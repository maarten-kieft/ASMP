@echo off

docker build -t blackhawkdesign/asmp-web-linarm:latest -f docker/linarm/Dockerfile-web-linarm .
docker build -t blackhawkdesign/asmp-processor-linarm:latest -f docker/linarm/Dockerfile-processor-linarm .
docker build -t blackhawkdesign/asmp-aggregator-linarm:latest -f docker/linarm/Dockerfile-aggregator-linarm .
docker build -t blackhawkdesign/asmp-updater-linarm:latest -f docker/linarm/Dockerfile-updater-linarm .

docker push blackhawkdesign/asmp-web-linarm:latest
docker push blackhawkdesign/asmp-processor-linarm:latest
docker push blackhawkdesign/asmp-aggregator-linarm:latest
docker push blackhawkdesign/asmp-updater-linarm:latest