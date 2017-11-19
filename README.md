# ElasticSec

## Overview

This project is a portable ELK stack that can be used together with Elastic's Beats plugins and other tools to process different kinds of security-related data into Elasticsearch. While other excellent tools exists for analyzing packet captures, logs, and other similar data, this project aims to use the Elastic stack to centralize the collection and analysis of this information. 

We think this can be useful for security analysts, malware researchers, incident responders, and others in the security field. As such, we plan on creating default configurations for the formats most commonly encountered by security folk.


### Features

- Pre-configured support for common data formats
    + [x] PCAP
    + [ ] Bro logs (TODO)
    + [ ] Syslog (TODO)
    + [ ] Nmap (TODO)
    + More...
- [ ] Custom index templates for Elasticsearch (TODO)
- [ ] Saved searches and visualizations of useful metrics (TODO)


## Setup

**Requirements:**  
- docker-compose

### Building the E+K Containers

The ELK containers are built using docker-compose. If you don't have it installed, look here for [instructions](https://docs.docker.com/compose/install/).

Run the following command in the root directory of the project (the one containing `docker-compose.yml`):

```
docker-compose up -d
```


## Processing PCAPs

### Installing Packetbeat

Packetbeat is the Beats plugin made specifically for packet capture data. Usually, it is run as a service and collects the packet captures in real time, but it can also be provided an input pcap file for reading.

Packetbeat can be installed through package manager repositories if you've added their repos to your sources list or by downloading a file in the appropriate format for your OS. 

The following commands download and install the Packetbeat package for Debian-based systems on your local machine.

```
sudo apt-get install libpcap0.8
curl -L -O https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.6.3-amd64.deb
sudo dpkg -i packetbeat-5.6.3-amd64.deb
```

Once Packetbeat is installed, there isn't much do configuration-wise. The defaults work out of the box for our setup, but changes can be made if needed.


### Usage

Once the containers are up and running, the pcap file can be provided to Packetbeat for processing. The Debian package provides a script named `packetbeat.sh` for running Packetbeat in the foreground. This may be different for other Linux flavors.

Run the following command, providing the path to the packet capture file:

```
packetbeat.sh -I /path/to/pcap
```

Navigate to `127.0.0.1:5601` in a browser. You will be presented with a screen asking you to create a default index template. Use `packetbeat-*` as the index template name. If everything worked correctly the settings will be applied and the data will be visible in the Discover tab. 