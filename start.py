#! /usr/bin/env python3

from sys import argv, stderr
from lib.aoc import cookie
from datetime import date
import time
import requests

def debug(*args, **kwargs):
    print(*args, **kwargs, file=stderr)

## Parse YEAR and DAY as command-line arguments
## Defaults to current YEAR/DAY if not specified

YEAR = date.today().year
DAY = date.today().day
if len(argv) > 1:
    DAY = int(argv[1])
if len(argv) > 2:
    YEAR = int(argv[2])

## Retrieve challenge input
## The script may be ran few seconds before challenge opening.
## It will attempt downloading the input every 5 seconds until it works

input_url = f"https://www.adventofcode.com/{YEAR}/day/{DAY}/input"
code = 404
input_text = ""

while code != 200:
    debug("GET", input_url, end = '... ')
    r = requests.get(input_url, cookies={"cookie":cookie})
    code = r.status_code
    input_text = r.text
    debug(code)
    time.sleep(5)

## Write the challenge input in the YEAR/DAY/input.txt file

with open(f"{YEAR}/{DAY}/input.txt", "w") as file:
    file.write(input_text)
