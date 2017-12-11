import subprocess


class InputReader:
    '''InputReader class'''

    def __init__(self, project):
        self.project = project
        self.readcmd = ''

        # Initial checks and configuration for input
        self.config(self.project.config.input_type)
        self.check_dependencies(self.project.config.input_type)

        self.read()

    
    # Read command, is passed 
    def read(self):
        if self.project.config.input_type == 'pcap':
            self.readcmd = "sudo /usr/share/packetbeat/bin/packetbeat -path.config {} -c packetbeat.yml -I {}".format(self.project.config.packetbeat_conf_path, self.project.config.input_
            subprocess.call(self.readcmd.split(' '))

        elif self.project.config.input_type == "syslog":
            
        
    
    def config(self, input_type):
        # subprocess.run(["sudo", "chown", "0:0"])
        pass


    def check_dependencies(self, input_type):
        pass
