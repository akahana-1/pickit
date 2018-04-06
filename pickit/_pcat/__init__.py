#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from signal import signal, SIGPIPE, SIG_DFL

from ..pickit import PickIt


def parse():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )

    parser.add_argument(
            "FILE",
            type=str,
            help="input file"
            )
    parser.add_argument(
            "-n",
            type=int,
            nargs="?",
            default=-1
            )

    return parser.parse_args()


def main():
    signal(SIGPIPE, SIG_DFL)
    args = parse()

    p = PickIt(args.FILE, args.n)

    for _ in p:
        if hasattr(_, "__str__"):
            print(str(_).replace("\n", " "))
        else:
            print(type(_))


