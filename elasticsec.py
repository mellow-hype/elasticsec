#!/usr/bin/env python3
import argparse
from src.project import Project

def cli_handle_arguments():
    '''This function handles command-line arguments.'''

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Subcommands', description='Available subcommands')

    # Project init subcommand parser
    proj_parser = subparsers.add_parser('new', help='Initialize a new project')
    proj_parser.add_argument('projectname', help='Name of new project')

    # Input subcommand parser
    input_parser = subparsers.add_parser('input', help='Read an input source')
    input_parser.add_argument('project', help='Target project')
    input_parser.add_argument('type',choices=['pcap', 'nmap'], 
                                help='Type of data to be read')
    input_parser.add_argument('input-path', help='Path to input data')

    # Container subcommand parser
    startup_parser = subparsers.add_parser('containers', help='Manage the Docker containers')
    startup_parser.add_argument('--up', help='Bring the containers up', action='store_true')
    startup_parser.add_argument('--stop', help='Stop the containers', action='store_true')
    startup_parser.add_argument('--restart', help='Restart the containers', action='store_true')
    startup_parser.add_argument('project', help='Target project')

    return parser.parse_args()



if __name__ == '__main__':

    args = cli_handle_arguments()

    # Handle argument to create a new project directory
    try:
        if args.projectname is not None:
            newProject = Project(args.projectname)

            if newProject.project_exists() is False:
                newProject.create_new_project_directory()
                exit()
    except AttributeError:
        currentProject = Project(args.project)


    # Handle container actions
    if args.up is True:
        currentProject.containers.start()
    elif args.stop is True:
        currentProject.containers.stop()
    elif args.restart is True:
        currentProject.containers.restart()

    # Handle input functions
    

