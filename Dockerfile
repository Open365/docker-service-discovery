FROM docker-registry.eyeosbcn.com/alpine6-node-base

COPY alpine-*.list /var/service/
COPY serf.py /bin/

ENV SERF_ADVERTISE_IP 172.17.42.1
ENV SERF_BIND_ADDRESS ""

RUN apk update && apk add python && \
    rm -r /var/cache/apk/* && \
    chmod +x /bin/serf.py

CMD /bin/serf.py

EXPOSE 7946/tcp 7946/udp
