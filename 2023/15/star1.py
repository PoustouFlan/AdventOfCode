import sys
sys.path.insert(0, "../../lib")
from aoc import submit

def hash(string):
    """
    HASH algorithm
    """
    result = 0
    for char in string:
        result += ord(char)
        result *= 17
        result %= 256
    return result

## Main
result = 0
for step in input().split(','):
    result += hash(step)

submit(result, 1, 15, 2023)
