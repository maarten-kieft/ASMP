docker build -t blackhawkdesign/asmp-web-lin64 -f docker/lin64/Dockerfile-web-lin64 .
docker build -t blackhawkdesign/asmp-processor-lin64 -f docker/lin64/Dockerfile-processor-lin64 .
docker build -t blackhawkdesign/asmp-aggregator-lin64 -f docker/lin64/Dockerfile-aggregator-lin64 .
docker build -t blackhawkdesign/asmp-updater-lin64 -f docker/lin64/Dockerfile-updater-lin64 .

docker push blackhawkdesign/asmp-web-lin64
docker push blackhawkdesign/asmp-processor-lin64
docker push blackhawkdesign/asmp-aggregator-lin64
docker push blackhawkdesign/asmp-updater-lin64