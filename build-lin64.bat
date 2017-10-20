@echo off

docker build -t blackhawkdesign/asmp-web-lin64:latest -f docker/lin64/Dockerfile-web-lin64 .
docker build -t blackhawkdesign/asmp-processor-lin64:latest -f docker/lin64/Dockerfile-processor-lin64 .
docker build -t blackhawkdesign/asmp-aggregator-lin64:latest -f docker/lin64/Dockerfile-aggregator-lin64 .
docker build -t blackhawkdesign/asmp-updater-lin64:latest -f docker/lin64/Dockerfile-updater-lin64 .

docker push blackhawkdesign/asmp-web-lin64:latest
docker push blackhawkdesign/asmp-processor-lin64:latest
docker push blackhawkdesign/asmp-aggregator-lin64:latest
docker push blackhawkdesign/asmp-updater-lin64:latest