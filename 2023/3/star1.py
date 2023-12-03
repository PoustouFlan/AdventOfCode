import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Reading the input
grid = sys.stdin.readlines()
n = len(grid)
m = len(grid[0])

# Add an extra border, remove '\n'
for y in range(n):
    grid[y] = '.' + grid[y][:-1] + '.'

extra_line = '.' * (m+2)
grid = [extra_line] + grid + [extra_line]

def extract(x, y):
    """
    Extracts the number that contains the digit at coordinates (x, y).
    Returns the first and last x-position of the number, and the number itself.
    """
    while grid[y][x].isdigit():
        x -= 1

    x += 1
    start = x
    number = ''

    while grid[y][x].isdigit():
        number += grid[y][x]
        x += 1

    return start, x, int(number)

def extract_part(x, y):
    """
    If the digit at coordinates (x, y) is part of a "part number",
    returns the part number itself and its last coordinate.

    Otherwise returns 0 as a number.
    """
    if not grid[y][x].isdigit():
        return 0, x+1

    start, end, number = extract(x, y)

    # Check if it is a part number
    for y2 in range(y-1, y+2):
        for x2 in range(start-1, end+1):
            if (y, start) <= (y2, x2) < (y, end):
                # (x2, y2) is part of the number itself
                continue

            if grid[y2][x2] != '.':
                # It is a part number
                return number, end

    # It is not a part number
    return 0, end


result = 0

for y in range(1, n+1):
    x = 1
    while x <= m:
        number, end = extract_part(x, y)
        x = end
        result += number

submit(result, 1, 3, 2023)
