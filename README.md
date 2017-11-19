# Elastify PCAPs

## Overview

This project gives you a portable Elasticsearch+Kibana stack that can be used together with Elastic's Packetbeat plugin to read packet capture files into Elasticsearch. While other excellent tools exists for analyzing packet capture data, Elasticsearch's query capabilites and Kibana's pretty and functional UI are a good addition to any toolset. The ability to get an overview of the data contained in a packet capture and easily search and create filters can really help speed up investigation processes, for example.

The long-term goal of the project is to create an extendable tool for security analysts, malware researchers, and others in the security field to use during investigations and other projects.


## Requirements

- docker-compose
- Packetbeat


## Setup

### Installing Packetbeat

Packetbeat is the Beats plugin made specifically for packet capture data. Usually, it is run as a service and collects the packet captures in real time, but it can also be provided an input pcap file for reading.

Packetbeat can be installed through package manager repositories if you've added their repos to your sources list or by downloading a file in the appropriate format for your OS. 

The following commands download and install the Packetbeat package for Debian-based systems.

```
sudo apt-get install libpcap0.8
curl -L -O https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.6.3-amd64.deb
sudo dpkg -i packetbeat-5.6.3-amd64.deb
```

Once Packetbeat is installed, there isn't much else to do with it configuration-wise. The defaults work out of the box for our setup, but changes can be made if needed.

### Build the E+K Containers

Next, we build the Docker containers using docker-compose. If you don't have it installed, look here for [instructions](https://docs.docker.com/compose/install/).

Run the following command in the root directory of the project (the one containing `docker-compose.yml`):

```
docker-compose up -d
```


## Usage

Once the containers are up and running, the pcap file can be provided to Packetbeat for processing. The Debian package provides a script named `packetbeat.sh` for running Packetbeat in the foreground. This may be different for other Linux flavors.

Run the following command, providing the path to the packet capture file:

```
packetbeat.sh -I /path/to/pcap
```

Navigate to `127.0.0.1:5601` in browser. You will be presented with a screen asking you to create a default index template. Use `packetbeat-*` as the index template name. If everything worked correctly the settings will be applied and the data will be visible in the Discover tab. 