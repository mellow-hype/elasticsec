import subprocess
from os import path
 

class Container:
    def __init__(docker_path):
        self.docker_path = docker_path
        self.status = 0
    
    def start(self):

        subprocess.check_output("cd", self.docker_path)
        subprocess.check_output("docker-compose" "up" "-d")

    
    def stop(self):

        subprocess.check_output("cd", self.docker_path)
        subprocess.check_output("docker-compose" "stop" "-d")


    def restart(self):

        subprocess.check_output("cd", self.docker_path)
        subprocess.check_output("docker-compose" "restart" "-d")


