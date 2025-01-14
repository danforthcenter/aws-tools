#!/usr/bin/env python

import argparse
import os, grp
import subprocess

def options():
    parser = argparse.ArgumentParser(description="Submit an interactive SOCA job.")
    #parser.add_argument("-f", "--filename", help="Filename and path to output jobfile.", default = 'intjob.sh')
    parser.add_argument("-n", "--name", help="Name of the job.", default="p-interactive")
    parser.add_argument("-t", "--type", help="Type of instance.", default="m5.large")
    parser.add_argument("-d", "--scratch", help="Scratch space (GB).", default=10)
    parser.add_argument("-s", "--spot", action="store_true", help="Use spot instances.")
    return parser.parse_args()


def main():
    # Get command line options
    args = options()

    # Get the user's group name
    group_name = grp.getgrgid(os.getgid()).gr_name

    # add spot variable
    if args.spot:
        spot_string = "-l spot_price=auto"
    else:
        spot_string = ""
        
    subprocess.run(['qsub', '-I', 
                    '-j', 'oe', 
                    '-V', 
                    '-N', args.name,
                    '-P', group_name,
                    '-q', 'normal',
                    '-l', 'nodes=1',
                    '-l', 'system_metrics=True',
                    '-l', 'spot_price=auto',
                    '-l', f'instance_type={args.type}',
                    '-l', f'scratch_size={args.scratch}',
                    spot_string])

if __name__ == '__main__':
    main()
