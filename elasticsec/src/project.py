import os
from shutil import copytree, copyfile
from .containers import Container
from .input import InputReader

ERR_PROMPT = '[-]'
SUCC_PROMPT = '[+]'

class Project:
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
            print("{} Error: Project directory already exists in {}".format(ERR_PROMPT, self.config.project_path))
            exit()
        else:
            print("{} Creating new project directory in {}".format(SUCC_PROMPT, self.config.project_path))

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

            # Copy the nmap elasticsearch template to the correct location
            self.config.init_nmap_template()


    def reader(self, input_type, input_path):
        self.config.input_type = input_type
        self.config.input_path = input_path
        InputReader(self)

    
class Config:
    '''Configuration class'''

    def __init__(self, project):
        # Configure paths
        self.base_projects_path = "projects/"
        self.template_path = "project-template/"
        self.project_path= "{}{}/".format(self.base_projects_path, project)
        self.project_config = "{}/config.yml".format(self.project_path)
        self.docker_path = "{}docker/".format(self.project_path)
        self.project_data_path = "{}data/".format(self.docker_path)
        self.project_input_path = "{}input/".format(self.project_data_path)
        self.input_config_path = "{}config/inputs/".format('')
        self.packetbeat_conf_path = "{}packetbeat/".format(self.input_config_path)
        self.bro_conf_path = "{}bro/".format(self.input_config_path)
        self.nmap_template_path = "{}nmap/elasticsearch_nmap_template.json".format(self.input_config_path)

        # Configure input settings
        self.input_type = ''
        self.input_path = ''

        self.packetbeat_bin = "/usr/share/packetbeat/bin/packetbeat"


    def init_nmap_template(self):
        dest_dir = self.project_data_path
        dest_path = "{}/{}".format(dest_dir, os.path.basename(self.nmap_template_path))
        if os.path.exists(dest_dir) is False:
            os.mkdir(dest_dir)
        copyfile(self.nmap_template_path, dest_path)


def list_projects():
    projects_path = str(os.getcwd() + "/projects")
    projects_list = os.listdir(projects_path)
    for p in projects_list:
        print(p)
