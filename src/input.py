class NewInput:
    
    def __init__(self, input_type, project):
        self.construct_input_config()
    
    def construct_input_config(input_type):
        if input_type == "pcap":
            self.pcap = PCAP()
        elif input_type == "nmap":
            pass
        elif input_type == "bro":
            pass


class PCAP:
    pass


class Bro:
    pass


class Nmap:
    pass