#!/usr/bin/env python3
import argparse
from os import path
 
def cli_handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--new-project", help="Create a new project directory", action="store", dest="project_path")
    parser.add_argument("type", help="Type of input to be read [default is pcap]", choices=['pcap'], default='pcap')


    args = parser.parse_args()
    if args.project_path is not None:
            print("New project path is: {}".format(args.project_path))
            exit()
    else:
        pass
    



if __name__ == '__main__':

    cli_handle_arguments()
