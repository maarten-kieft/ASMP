FROM resin/rpi-raspbian:jessie-20160831
RUN apt-get update && apt-get install -y python3 python3-pip
RUN mkdir -p /usr/bin/asmp/data
COPY src /usr/bin/asmp/
VOLUME /usr/bin/asmp/data
RUN pip3 install -r /usr/bin/asmp/requirements.txt
EXPOSE 8000
CMD ["/usr/bin/asmp/start-arm.sh"]