import os
from shutil import copytree
from .containers import Container
from .input import InputReader

ERR_PROMPT = '[-]'
SUCC_PROMPT = '[+]'

class Project():
    '''Project class'''

    def __init__(self, project_name):
        self.name = project_name
        self.config = Config(self.name)
        self.containers = Container(self.config.docker_path)

    # Check if current project exists
    def project_exists(self):
        if os.path.exists(self.config.project_path): 
            return True
        else:
            return False


    def create_new_project_directory(self):
        # Check if project directory already exists
        if self.project_exists() is True:
            print("{} Error: Project directory already exists at {}".format(ERR_PROMPT, self.config.project_path))
            exit()
        else:
            print("Creating new project directory at {}".format(self.config.project_path))

            # Make sure other directories are present
            if os.path.exists(self.config.base_projects_path) is False:
                os.makedirs(self.config.base_projects_path)
            else:
                os.mkdir(self.config.project_path)

            # Copy Docker template files to new project
            copytree(self.config.template_path, self.config.docker_path)

            # Create the data directory
            os.mkdir(self.config.docker_path + '/elasticsearch/data')

            # Create the data and inputs directory for the new project
            os.makedirs(self.config.project_input_path)
    
    def reader(self, input_type, input_path):
        self.config.input_type = input_type
        self.config.input_path = input_path
        InputReader(self)

    
class Config:
    '''Configuration class'''

    def __init__(self, project):
        # Configure paths
        self.base_projects_path = self.set_base_projects_path()
        self.template_path = self.set_template_path()
        self.project_path= str(self.base_projects_path + project)
        self.docker_path = str(self.project_path + "/docker")
        self.project_data_path = str(self.docker_path + "/data")
        self.project_input_path = str(self.project_data_path + "/input")
        self.project_config = str(self.project_path + "config.yml")
        self.input_config_path = self.set_input_config_path()
        self.packetbeat_conf_path = self.input_config_path + "/packetbeat/"
        self.bro_conf_path = self.input_config_path + "/bro/"
        self.nmap_conf_path = self.input_config_path + "/nmap/"

        # Configure input settings
        self.input_type = ''
        self.input_path = ''

        self.packetbeat_bin = "/usr/share/packetbeat/bin/packetbeat"


    # Set path to directory where projects will be stored
    def set_base_projects_path(self):
        return str(os.getcwd()) + '/projects/'


    # Set path to directory where project templates are stored
    def set_template_path(self):
        return str(os.getcwd() + '/project-template/')


    def set_input_config_path(self):
        return str(os.getcwd() + '/config/inputs')



def list_projects():

    projects_path = str(os.getcwd() + "/projects")
    projects_list = os.listdir(projects_path)
    for p in projects_list:
        print(p)