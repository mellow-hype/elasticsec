class Project:
    def __init__(self, project_name, project_path): 
        self.path = project_path
        self.name = project_name
    

    def new_project(self):
        build_project(self.path)
    

    def create_project_dirs(self):
        pass
    

    def build_project(self):
        create_project_dirs()