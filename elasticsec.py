#!/usr/bin/env python3
import argparse
from src.project import Project

def cli_handle_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("project", 
                         help="Target project") 
    parser.add_argument("type", 
                         help="Type of input to be read [default is pcap]",
                         choices=['pcap'])
    parser.add_argument("input", 
                         help="Path to input file to be read")
    
    return parser.parse_args()


if __name__ == '__main__':

    cli_args = cli_handle_arguments()
    currentProject = Project(cli_args.project)
    
    