import subprocess

class InputReader:

    def __init__(self):
        self.pcap = PCAP()
        self.bro = BroInput()
        self.nmap = Nmap()


class PCAP:
    def __init__(self):
        pass


    def config(self):
        pass
    

    def check_dependencies(self):
        pass


    def read(self):
        # subprocess.run(["sudo", "chown", "0:0"])
        pass
        
        


class BroInput:
        pass


class Nmap:
        pass