import requests
import os.path
from datetime import date
from sys import stderr

def debug(*args, **kwargs):
    print(*args, **kwargs, file=stderr)

## Retrive session cookie
path = os.path.abspath(os.path.dirname(__file__))
cookie_path = os.path.join(path, "cookie.txt")

cookie = None
with open(cookie_path, "r") as cookie_file:
    cookie = cookie_file.read().strip()


def submit(value, level=None, day=None, year=None):
    """
    Automatically submit a value for a challenge.
    year/day are set to current day if not provided.
    level = 1 for the gray star, level = 2 for the golden star.
    level = None for attempting both.
    """
    if year is None:
        year = date.today().year

    if day is None:
        day = date.today().day

    if level is None:
        levels = [2, 1]
    else:
        levels = [level]

    for level in levels:
        submit_url = f"https://adventofcode.com/{year}/day/{day}/answer"
        debug("Submitting", value, "to", submit_url, "...")
        payload = {
            "level": level,
            "answer": value,
        }
        r = requests.post(submit_url, payload, cookies={"cookie":cookie})
        debug(r.status_code)
        debug(r.text)
