import os
from shutil import copytree

class Project:
    def __init__(self, project_name):
        self.project_storage_dir = self.set_project_storage_path()
        self.templates_dir = self.set_template_path()
        self.name = project_name
        self.path = str(self.project_storage_dir + self.name)

    # Set path to directory where projects will be stored
    def set_project_storage_path(self):
        return str(os.getcwd()) + '/projects/'

    # Check if path to directory for project storage exists
    def projects_storage_path_exists(self):
        if os.path.exists(self.project_storage_dir) and os.path.isdir(os.getcwd() + '/projects/'):
            return True
        else:
            return False
    
    # Set path to directory where project templates are stored
    def set_template_path(self):
        return str(os.getcwd() + '/elk-containers/')

    
    # Check if current project exists
    def project_exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    
        

        

        
