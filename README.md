# ElasticSec

## Overview

Elasticsec is a portable ELK stack that can be used together with Elastic's Beats plugins and other tools to process different kinds of security-related data into Elasticsearch. While other excellent tools exists for analyzing packet captures, logs, and other similar data, this project aims to use the Elastic stack to centralize the collection and analysis of this information. 

This might be useful to security analysts, malware researchers, incident responders, and others in the security field. As such, the plan is to create default configurations for the formats most commonly encountered by security folk.


### Requirements    
- Python 3
- docker-compose


### Features

- Pre-configured support for common data formats
    + [x] PCAP
    + [x] Syslog (added 2017-12-11)
    + [x] Bro
        + [x] HTTP
    + [ ] Nmap (TODO)
    + More...
- [ ] Custom index templates for Elasticsearch 
- [ ] Saved searches and visualizations of useful metrics 


## Usage

### Initialize a New Project

```
./elasticsec.py new <project_name>
```

### Start the Containers

```
./elasticsec.py containers --up <project_name>
```


## Processing PCAPs

### Install Packetbeat

Use the following commands to download and install the Packetbeat package for Debian-based systems:

```
sudo apt-get install libpcap0.8
curl -L -O https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.6.3-amd64.deb
sudo dpkg -i packetbeat-5.6.3-amd64.deb
```

Or use these for RPM-based systems:

```
sudo yum install libpcap
curl -L -O https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.6.3-x86_64.rpm
sudo rpm -vi packetbeat-5.6.3-x86_64.rpm
```

Once Packetbeat is installed, there isn't much do configuration-wise. The defaults work out of the box for our setup, but changes can be made if needed.

See the [Packetbeat documentation]() for more information.

### Usage

Once the containers are up and running, the pcap file can be provided to Packetbeat for processing. 

```
./elasticsec.py input <project> pcap /path/to/pcap 
``` 


## Processing Syslog Files

### Usage 

Once containers are up and running, you can use the input subcommand to send the syslog file to Logstash for processing.

```
./elasticsec.py input <project> syslog /path/to/syslog_file
```



## Processing Bro Log Files

### Bro HTTP Log

Once containers are up and running, you can use the input subcommand to copy the Bro file to the data input directory Logstash is monitoring.

```
./elasticsec.py input <project> bro /path/to/bro_http_file
```

*Note: Make sure the file name includes the string 'http', as this is how Logstash identifies the log type.*