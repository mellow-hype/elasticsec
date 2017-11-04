FROM docker.elastic.co/beats/packetbeat:5.6.3
USER packetbeat
RUN /usr/share/packetbeat/packetbeat -e \
     -c /usr/share/packetbeat/packetbeat.yml -t \
     -I /usr/share/packetbeat/data/*.pcap
