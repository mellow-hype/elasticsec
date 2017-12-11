import subprocess
import socket
from os import path

HOST_IP = '127.0.0.1'
HOST_PORT_SYSLOG = 5000


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
            self.readcmd = \
                "sudo /usr/share/packetbeat/bin/packetbeat -path.config {} -c packetbeat.yml -I {}".format(
                    self.project.config.packetbeat_conf_path, 
                    self.project.config.input_path
                )
            subprocess.call(self.readcmd.split(' '))

        elif self.project.config.input_type == 'syslog':
            send_syslog_tcp_input(self.project.config.input_path)

        else:
            print("{} is not a supported type.".format(self.project.config.input_type))
            exit()
        
    
    def config(self, input_type):
        # subprocess.run(["sudo", "chown", "0:0"])
        pass


    def check_dependencies(self, input_type):
        pass


def send_syslog_tcp_input(input_path):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST_IP, HOST_PORT_SYSLOG))

    if path.isfile(input_path):
        f = open(input_path, "rb")

        while True:
            data = f.read()
            if not data: break
            sock.sendall(data)
        
        f.close()
        print("{} sent to Logstash syslog input".format(input_path))

    else:
        print("File not found.")
    
    sock.close()
