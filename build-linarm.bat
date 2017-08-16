docker build -t blackhawkdesign/asmp-web-linarm -f docker/linarm/Dockerfile-web-linarm .
docker build -t blackhawkdesign/asmp-processor-linarm -f docker/linarm/Dockerfile-processor-linarm .
docker build -t blackhawkdesign/asmp-aggregator-linarm -f docker/linarm/Dockerfile-aggregator-linarm .
docker build -t blackhawkdesign/asmp-updater-linarm -f docker/linarm/Dockerfile-updater-linarm .

docker push blackhawkdesign/asmp-web-linarm
docker push blackhawkdesign/asmp-processor-linarm
docker push blackhawkdesign/asmp-aggregator-linarm
docker push blackhawkdesign/asmp-updater-linarm