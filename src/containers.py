import subprocess
from os import chdir

class Container:
    def __init__(self, docker_path):
        self.docker_path = docker_path
        self.status = 0


    def start(self):
        '''Start the containers'''

        chdir(self.docker_path)
        subprocess.run(["docker-compose", "up", "-d"])

    
    def stop(self):
        '''Bring the containers down'''

        chdir(self.docker_path)
        subprocess.run(["docker-compose", "stop"])


    def restart(self):
        '''Restart the containers'''

        chdir(self.docker_path)
        subprocess.run(["docker-compose", "restart"])


