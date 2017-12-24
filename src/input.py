import subprocess
import socket
from os import path, makedirs, mkdir
from shutil import copyfile

HOST_IP = '127.0.0.1'
HOST_PORT_SYSLOG = 5000

ERR_PROMPT = '[-]'
SUCC_PROMPT = '[+]'


class InputReader:
    '''InputReader class'''

    def __init__(self, project):
        self.project = project
        self.readcmd = ''

        # Initial checks and configuration for input
        self.config()
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

        elif self.project.config.input_type == 'bro':
            src_file = self.project.config.input_path
            dst_dir = (self.project.config.project_input_path + "/{}/{}".format(
                self.project.config.input_type, 
                src_file.rstrip('/').split('/')[-1])
                )

            copyfile(src_file, dst_dir)
        
    
    def config(self):
        if self.project.config.input_type == 'pcap':
            pass

        elif self.project.config.input_type == 'syslog':
            pass

        elif self.project.config.input_type == 'bro':
            init_bro_dirs(self.project.config.project_input_path)

        else:
            print("{} '{}' is not a supported type.".format(ERR_PROMPT, self.project.config.input_type))
            exit()

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
        print("{} File sent to Logstash syslog input: {}".format(SUCC_PROMPT, input_path))

    else:
        print("{} File not found: {}".format(ERR_PROMPT, input_path))
    
    sock.close()


def init_bro_dirs(inputs_dir):
    bro_input_path = inputs_dir + '/bro'
    if path.exists(bro_input_path) is False:
        makedir(bro_input_path)
    else:
        pass
        


