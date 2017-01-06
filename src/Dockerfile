FROM httpd:2.4
RUN apt-get update
RUN apt-get --assume-yes install python3
RUN apt-get --assume-yes install python3-dev
RUN apt-get --assume-yes install wget
COPY .install-modwsgi.sh /usr/bin/
RUN /usr/bin/install-modwsgi.sh