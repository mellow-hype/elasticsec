#!/usr/bin/env python3
import argparse
from src.project import Project

def cli_handle_arguments():
    '''This function handles command-line arguments.'''

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Subcommands', description='Available subcommands')

    # Project init subcommand parser
    proj_parser = subparsers.add_parser('new', help='Initialize a new project')
    proj_parser.add_argument('new_project_name', help='Name of new project')

    # Input subcommand parser
    input_parser = subparsers.add_parser('input', help='Read an input source')
    input_parser.add_argument('type',choices=['pcap', 'nmap'], 
                                help='Type of data to be read')
    input_parser.add_argument('input-path', help='Path to input data')

    # Container subcommand parser
    startup_parser = subparsers.add_parser('containers', help='Manage the Docker containers')
    startup_parser.add_argument('--up', help='Bring the containers up', action='store_true')
    startup_parser.add_argument('--down', help='Stop the containers', action='store_true')
    startup_parser.add_argument('--restart', help='Restart the containers', action='store_true')
    startup_parser.add_argument('project-path', help='Path to target project directory')

    args = parser.parse_args()

    if args.new_project_name is not None:
        newProject = Project(args.new_project_name)

        if newProject.project_exists() is False:
            newProject.create_new_project_directory()

        exit()


if __name__ == '__main__':

    cli_handle_arguments()

