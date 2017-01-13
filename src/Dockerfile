FROM python:3
RUN mkdir /usr/bin/asmp
RUN mkdir /usr/bin/data
COPY ./web /usr/bin/asmp/web
COPY ./worker /usr/bin/asmp/worker
COPY ./asmp /usr/bin/asmp/asmp
COPY requirements.txt manage.py start.sh data/db.sqlite3 /usr/bin/asmp
VOLUME ["/usr/bin/amp/data:/usr/bin/amp/data"]
RUN pip install -r /usr/bin/asmp/requirements.txt
EXPOSE 8000
CMD ["/usr/bin/asmp/start.sh"]
