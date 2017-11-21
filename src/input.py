from .project import Project
import subprocess

class InputReader:
    
    def __init__(self, project, input_type, input_path):
        self.project = Project(self.project)
        self.type = input_type
        self.input_path = input_path
    
    def read_input(self):
        if self.type == "pcap":
            self.pcap()
        elif self.type == "nmap":
            self.nmap()
        elif self.type == "bro":
            self.bro()

    def check_dependencies(self):
        pass


    def pcap(self):


    def bro(self):
        pass

    def nmap(self):
        pass