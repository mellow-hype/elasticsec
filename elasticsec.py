#!/usr/bin/env python3
import argparse
from src.project import Project, list_projects

def cli_handle_arguments():
    '''This function handles command-line arguments.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', help='List projects', action='store_true')
    subparsers = parser.add_subparsers(title='Subcommands', description='Available subcommands')

    # Project init subcommand parser
    proj_parser = subparsers.add_parser('new', help='Initialize a new project')
    proj_parser.add_argument('projectname', help='Name of new project')

    # Input subcommand parser
    input_parser = subparsers.add_parser('input', help='Read an input source')
    input_parser.add_argument('project', help='Target project')
    input_parser.add_argument('intype',choices=['pcap', 'nmap'], 
                                help='Type of data to be read')
    input_parser.add_argument('inputpath', help='Path to input data')

    # Container subcommand parser
    startup_parser = subparsers.add_parser('containers', help='Manage the Docker containers')
    startup_parser.add_argument('--start', help='Bring the containers up', action='store_true')
    startup_parser.add_argument('--stop', help='Stop the containers', action='store_true')
    startup_parser.add_argument('--restart', help='Restart the containers', action='store_true')
    startup_parser.add_argument('project', help='Target project')

    return parser.parse_args()



if __name__ == '__main__':

    # Get values from cmd-line arguments
    args = cli_handle_arguments()

    try:
        if args.list is True:
            list_projects()
    except AttributeError or KeyboardInterrupt:
        pass

    try:
        if args.projectname is not None:
            newProject = Project(args.projectname).create_new_project_directory()
    except AttributeError or KeyboardInterrupt:
        pass

    try:   
        if args.intype is not None:
            currentProject = Project(args.project)
            currentProject.reader(args.intype, args.inputpath)
    except AttributeError or KeyboardInterrupt:
        pass

    try:
        if args.start is True:
            currentProject = Project(args.project)
            currentProject.containers.start()
        elif args.stop is True:
            currentProject = Project(args.project)
            currentProject.containers.stop()
        elif args.restart is True:
            currentProject = Project(args.project)
            currentProject.containers.restart()
    except AttributeError or KeyboardInterrupt:
        pass


    
    

