FROM docker.elastic.co/beats/packetbeat:5.6.3
USER root
RUN mkdir /usr/share/packetbeat/data
RUN chown packetbeat /usr/share/packetbeat/data
RUN chown packetbeat /usr/share/packetbeat/packetbeat.yml
USER packetbeat
RUN packetbeat -e -c /usr/share/packetbeat/packetbeat.yml -t -I /usr/share/packetbeat/data/*.pcap -d "publish"
