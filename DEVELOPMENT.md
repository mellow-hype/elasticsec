# Development 

## Components

1. Docker containers
2. Wrapper script


## Feature Goals

1. Configurations for common formats
    + Logstash filters
    + Index templates
    + Visualizations/Saved searches
2. Supported formats
    + [ ] PCAP
        + Index templates
        + Visualizations/Saved searches
    + [ ] Syslog
    + [ ] Bro logs
        + Logstash filters
        + Index templates
        + Visualizations/Saved searches
    + [ ] Nmap
        - Requires installation of the Logstash nmap codec via `logstash-plugin` tool
3. Wrapper script
    + [x] Allow for selection of input mode via flags
    + [x] "Projects" feature to automate the process of writing persistent data to separate directories to allow for multiple projects



## Task Tracking

- Configuration
    - [ ] Generate config
    - [ ] Read config
    - [ ] Edit config
    - [ ] Write config
- Projects
    - [x] Create project directory
    - [x] Copy Docker files
- Inputs
    - [ ] Check dependencies
    - [ ] Error handling
    - [x] PCAP
        - [x] Custom packetbeat.yml
            - `sudo chown 0:0 packetbeat.yml`
            - `sudo chmod go-w packetbeat.yml`
        - [x] Custom Packetbeat index template
        - [x] Launch Packetbeat
    - Bro
        - [ ] Create default LS pipeline for Bro
