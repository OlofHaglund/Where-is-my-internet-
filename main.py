#!/usr/bin/env python3

import os
import datetime
import time

from dataclasses import dataclass

def print_end(start, string):
    with open("output.txt", "a") as file:
        file.write(f"Connectivity is {string}")
        file.write(f"Start: {start}")
        end = datetime.datetime.now()
        file.write(f"End: {end}")
        file.write(f"Duration: {end - start} ")

def main():
    up = True
    start = datetime.datetime.now()
    sleep = 10

    hostname = "olofhaglund.name"

    with open("output.txt", "w") as file:
        file.write(f"Monitoring started {datetime.datetime.now()} with pings toward {hostname} every {sleep} seconds")


    while True:
        response = os.system(f"ping -c 1 {hostname}")

        if response == 0:
            if not up:
                print_end(start, "up")
                start = datetime.now()
                up = True
        else:
            if up:
                print_end(start, "lost")
                start = datetime.now()
                up = False
        time.sleep(sleep)

if __name__ == '__main__':
    main()
