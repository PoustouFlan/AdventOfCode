#! /usr/bin/env python3

from sys import argv, stderr
from lib.aoc import cookie
from datetime import date
import time
import requests

def debug(*args, **kwargs):
    print(*args, **kwargs, file=stderr)

YEAR = date.today().year
DAY = date.today().day
if len(argv) > 1:
    DAY = int(argv[1])
if len(argv) > 2:
    YEAR = int(argv[2])

input_url = f"https://www.adventofcode.com/{YEAR}/day/{DAY}/input"
code = 404

while code != 200:
    debug("GET", input_url, end = '... ')
    r = requests.get(input_url, cookies={"cookie":cookie})
    code = r.status_code
    debug(code)
    time.sleep(5)

with open(f"{YEAR}/{DAY}/input.txt", "w") as file:
    file.write(r.text)
