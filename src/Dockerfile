FROM httpd:2.4
RUN apt-get update
RUN apt-get --assume-yes install python python3 python3-dev build-essential
RUN mkdir /usr/bin/asmp
COPY mod_wsgi-4.5.13.tar.gz /usr/bin/asmp/mod_wsgi-4.5.13.tar.gz
COPY install-modwsgi.sh /usr/bin/asmp/install-modwsgi.sh
RUN /usr/bin/asmp/install-modwsgi.sh