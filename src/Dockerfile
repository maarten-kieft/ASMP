FROM python:3
RUN mkdir /usr/bin/asmp
RUN mkdir /usr/bin/data
COPY ./web /usr/bin/asmp/web
COPY ./worker /usr/bin/asmp/worker
COPY ./asmp /usr/bin/asmp/asmp
COPY ./manage.py /usr/bin/asmp
COPY ./requirements.txt /usr/bin/asmp
COPY ./start.sh /usr/bin/asmp
COPY ./db.sqlite3 /usr/bin/asmp
VOLUME ["/usr/bin/amp/data:/usr/bin/amp/data"]
RUN pip install -r /usr/bin/asmp/requirements.txt
EXPOSE 8000
CMD ["/usr/bin/asmp/start.sh"]
CMD ["python", "/usr/bin/asmp/manage.py", "worker"]
