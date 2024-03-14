#!/usr/bin/env python3

import os
import sys

color_green  = "\033[38;2;0;255;0m"
color_red    = "\033[38;2;255;0;0m"
color_yellow = "\033[38;2;255;255;0m"
term_color   = "\033[00m"

def log_error(args, **kwargs):
    if type(args) in (list, dict, tuple):
        print("wrong type of args to function")
    else:
        print(color_red + str(args) + term_color, file=sys.stderr, **kwargs)
    exit(1)

def log_warn(args, **kwargs):
    if type(args) in (list, dict, tuple):
        print("wrong type of args to function")
        exit(1)
    print(color_yellow + str(args) + term_color, file=sys.stderr, **kwargs)

def main():
    # HOME = os.environ["HOME"]
    dir = os.path.join(os.environ["HOME"], "Pictures/tests")
    extensions = ["jpg", "png", "jpeg"]

    if not os.path.exists(dir):
        log_error("no such directory: '%s'" % dir)

    for f in os.listdir(dir):
        f = os.path.join(dir, f)
        print("extension: %s" % f.rsplit('.', 1)[-1])
        if not f.rsplit('.', 1)[-1] in extensions or not os.path.isfile(f):
            continue
        log_warn(f)


if __name__ == "__main__":
    main()
