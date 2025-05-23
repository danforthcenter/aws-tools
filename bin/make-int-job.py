#!/usr/bin/env python

import argparse
import os, grp


def options():
    parser = argparse.ArgumentParser(description="Submit an interactive SOCA job.")
    parser.add_argument("-f", "--filename", help="Filename and path to output jobfile.", default = 'intjob.sh')
    parser.add_argument("-n", "--name", help="Name of the job.", default="interactive")
    parser.add_argument("-t", "--type", help="Type of instance.", default="m5.large")
    parser.add_argument("-d", "--scratch", help="Scratch space (GB).", default=10)
    parser.add_argument("-s", "--spot", action="store_true", help="Use spot instances.")
    return parser.parse_args()


def main():
    # Get command line options
    args = options()

    # Get the user's group name
    group_name = grp.getgrgid(os.getgid()).gr_name

    with open(args.filename, "w") as fp:
        fp.write("#!/bin/bash\n")
        fp.write("## BEGIN PBS SETTINGS: Note PBS lines MUST start with #\n")
        fp.write(f"#PBS -N {args.name}\n")
        fp.write(f"#PBS -V -j oe -o {args.name}.qlog\n")
        fp.write(f"#PBS -P {group_name}\n")
        fp.write("#PBS -q normal\n")
        fp.write("#PBS -l nodes=1\n")
        fp.write(f"#PBS -l instance_type={args.type}\n")
        fp.write("#PBS -l system_metrics=True\n")
        if args.scratch is not None:
            fp.write(f"#PBS -l scratch_size={args.scratch}\n")
        if args.spot:
            fp.write("#PBS -l spot_price=auto\n")
        fp.write("## END PBS SETTINGS\n")
        fp.write("## BEGIN JOB\n\n")
        fp.write("## END JOB\n")


if __name__ == '__main__':
    main()
