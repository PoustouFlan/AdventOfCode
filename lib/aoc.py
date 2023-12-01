import requests
from datetime import date
from sys import stderr
def debug(*args, **kwargs):
    print(*args, **kwargs, file=stderr)

cookie = None
with open("aoc.py", "r") as cookie_file:
    cookie = cookie_file.read()

def submit(value, level=1, year=None, day=None):
    """
    Automatically submit a value for a challenge.
    year/day are set to current day if not provided.
    level = 1 for the gray star, level = 2 for the golden star.
    """
    if year is None:
        year = date.today().year
        day = date.today().day

    submit_url = f"https://adventofcode.com/{year}/day/{day}/answer"
    debug("Submitting to", submit_url, "...")
    r = requests.post(submit_url, {"level": level, "answer": value}, cookies={"cookie":cookie})
    debug(r.status_code)
    debug(r.text)
    return r.status_code == 200
