FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    	nginx \
    	python3.6 \
    	python3-pip

ENV DBHOST="localhost" \
    DBUSER="root" \
    DBPASSWORD="password" \
    DBDATABASE="falcon-rbac" \
    DBPORT=3306 \
    DBPOOLSIZE=10 \
    DBECHO="False"

RUN mkdir -p /app/app
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.7.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

RUN mkdir -p /etc/nginx/sites-enabled && \
	mkdir -p /var/run/s6/uncaught-logs-fifo && \
	mkdir -p /var/log/s6-uncaught-logs && \
	chmod -R 777 /var/log/s6-uncaught-logs

RUN rm /etc/nginx/sites-enabled/default | true
COPY docker/nginx.conf /etc/nginx/sites-enabled
COPY docker/s6 /etc/s6/services

RUN chmod -R 777 /etc/s6/services

COPY . /app/

ENTRYPOINT ["/bin/s6-svscan","/etc/s6/services"]
CMD []