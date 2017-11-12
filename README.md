# Elastify PCAPs

## Overview

If you've ever taken a packet capture, you know that just a short amount of time spent capturing packets off the wire can produce a huge amount of data. While there are excellent tools available for viewing packet captures such as Wireshark, these tools are aimed at providing a microscopic view of the data. Sometimes it's valuable to get a macroscopic view, and this is where the power of Kibana's visualizations paired with Elasticsearch really shine. Together, they make a great tool for quickly visualizing the data contained in a pcap and searching through it in a nice UI. 

This project gives you a portable Elasticsearch+Kibana stack that you can use together with one of Elastic's Beats plugins, Packetbeat, to read a packet capture file and forward it to the local Elasticsearch instance for viewing in Kibana.

## Requirements

- docker-compose
- Packetbeat


## Setup

### Install Packetbeat

Packetbeat is one of the plugins in the Beats family. These are plugins that are basically transport agents that forward collected data to ingestion points such as Logstash or Elasticsearch. Packetbeat in particular is the Beats plugin made for dealing with packet capture data. Usually, it is run as a service and collects and processes the packet captures in real time, but it can also be provided an input pcap file for reading. The latter is the way in which we'll be using it.

Packetbeat can be installed through package manager repositories if you've added their repos to your sources lists or by downloading a file in the format appropriate for your OS. For Debian based systems, the following commands install the .deb package without having to add sources to your apt.

```
sudo apt-get install libpcap0.8
curl -L -O https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.6.4-amd64.deb
sudo dpkg -i packetbeat-5.6.4-amd64.deb
```

Once Packetbeat is installed, there isn't much else to do with it configuration-wise. The defaults work very well out of the box for our setup, but feel free to make changes if you'd like to. 

### Build the E+K Containers

Next, we build the Docker containers using docker-compose. If you don't have it installed, look here for [instructions](https://docs.docker.com/compose/install/).

Run the following command in the root directory of the project (the one containing docker-compose.yml):

```
docker-compose up -d
```


## Usage

Once the containers are up and running, it's time to read a packet capture into Packetbeat and get it processed into Elasticsearch. The Debian package provides a script `packetbeat.sh` for running Packetbeat in the foreground. This may be different for other Linux flavors.

Run the following command, providing the path to the packet capture file:

```
packetbeat.sh -I /path/to/pcap
```