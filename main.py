#!/usr/bin/env python3

import os
import datetime

from dataclasses import dataclass

def print_end(start, string):
    print(f"Connectivity is {string}")
    print(f"Start: {start}")
    end = datetime.datetime.now()
    print(f"End: {end}")
    print(f"Duration: {end - start} ")

def main():
    up = True
    start = datetime.datetime.now()

    hostname = "olofhaglund.name"
    response = os.system(f"ping -c 1 {hostname}")

    if response == 0:
        if !uptime.up:
            print_end(start, "up")
            start = datetime.now()
            up = True
    else:
        if uptime.up:
            print_end(start, "lost")
            start = datetime.now()
            up = False

if __name__ == '__main__':
    main()
