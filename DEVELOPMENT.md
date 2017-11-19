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

+ [ ] Allow for selection of input mode via flags, desired storage location, etc.
+ [ ] Handle separation of inputs by writing each input type to separate indexes
+ [ ] Automate Logstash pipeline construction (input, filter, output) based on input mode selected, if LS is required
+ [ ] "Projects" feature to automate the process of writing persistent data to separate directories to allow for multiple projects



