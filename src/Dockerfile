FROM httpd:2.4
RUN apt-get update
RUN apt-get --assume-yes install python3
RUN apt-get --assume-yes install python3-dev
RUN apt-get --assume-yes install wget
RUN mkdir /usr/bin/asmp
COPY install-modwsgi.sh /usr/bin/asmp/install-modwsgi.sh
RUN /usr/bin/asmp/install-modwsgi.sh