FROM docker-registry.eyeosbcn.com/alpine6-node-base

COPY alpine-*.list /var/service/
COPY serf.py /bin/

ENV SERF_ADVERTISE_IP 172.17.42.1
ENV SERF_BIND_ADDRESS ""

RUN cd /tmp && \
    apk update && \
    /scripts-base/buildDependencies.sh --production --install && \
    curl -L https://releases.hashicorp.com/serf/0.6.4/serf_0.6.4_linux_amd64.zip -o serf.zip && \
    unzip serf.zip && \
    rm serf.zip && \
    cp serf /usr/bin/serf && \
    /scripts-base/buildDependencies.sh --production --purgue && \
    chmod +x /bin/serf.py

CMD /bin/serf.py

EXPOSE 7946/tcp 7946/udp
