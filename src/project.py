import os
from shutil import copytree

class Project:
    def __init__(self, project_name):
        self.project_storage_dir = self.set_project_storage_path()
        self.templates_dir = self.set_template_path()
        self.name = project_name
        self.path = str(self.project_storage_dir + self.name)
        self.docker_path = str(self.path + "/docker")
        self.project_exists()

    # Set path to directory where projects will be stored
    def set_project_storage_path(self):
        return str(os.getcwd()) + '/projects/'


    # Set path to directory where project templates are stored
    def set_template_path(self):
        return str(os.getcwd() + '/elk-containers/')

    # Check if current project exists
    def project_exists(self):
        if os.path.exists(self.path): 
            print("Project exists, continuing...")
            return True
        else:
            return False

    def create_new_project_directory():
        print("Creating new project directory at {}".format(self.path))
        if os.path.exists(self.project_storage_dir) is False:
            os.makedirs(self.path)
        else:
            os.mkdir(self.path)
        copytree(self.templates_dir, self.docker_path)
        

        

        
