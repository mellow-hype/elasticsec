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
    + [ ] Syslog
    + [ ] Bro logs
    + [ ] Nmap
        - Requires installation of the Logstash nmap codec via `logstash-plugin` tool
3. Wrapper script

---
## Wrapper Script

### Features  

+ [x] Allow for selection of input mode via flags
+ [x] "Projects" feature to automate the process of writing persistent data to separate directories to allow for multiple projects

Configuration can be handled with a config file. This is generated whenever a new project is created and is used to enable input types. Settings made in this file inform the script about which components to build and which configurations to use. This way, each ELK stack is customized to the project. Changes can be made to the config file and the containers rebuilt in order to add functionality if needed.


### Task Tracking

- Configuration
    - Generate config
    - Read config
    - Edit config
    - Write config
- Projects
    - Create project directory
    - Copy Docker files
- Inputs
    - Check dependencies
    - Error handling
    - PCAP
        - Custom packetbeat.yml
            - `sudo chown 0:0 packetbeat.yml`
            - `sudo chmod go-w packetbeat.yml`
        - Custom Packetbeat index template
        - Launch Packetbeat
            - `sudo packetbeat.sh -path.config inputs/packetbeat/ -c packetbeat.yml -I /path/to/pcap`
    - Bro
        - Create default LS pipeline for Bro
        - 
