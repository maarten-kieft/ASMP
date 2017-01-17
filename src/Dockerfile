FROM resin/rpi-raspbian:jessie-20160831
RUN apt-get update
RUN apt-get install python3 python3-pip
RUN mkdir -p /usr/bin/asmp/data
COPY web /usr/bin/asmp/web
COPY worker /usr/bin/asmp/worker
COPY asmp /usr/bin/asmp/asmp
COPY requirements.txt manage.py start-arm.sh data/db.sqlite3 /usr/bin/asmp/
VOLUME ["/usr/bin/asmp/data:/usr/bin/asmp/data"]
RUN pip3 install -r /usr/bin/asmp/requirements.txt
EXPOSE 8000
CMD ["/usr/bin/asmp/start-arm.sh"]