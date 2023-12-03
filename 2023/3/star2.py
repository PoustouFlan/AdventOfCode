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

def extract_ratio(x, y):
    """
    If the digit at coordinates (x, y) is a gear, returns its gear ratio.

    Otherwise returns 0.
    """

    if grid[y][x] != '*':
        return 0

    numbers = []
    skip_until = (-1, -1)
    for y2 in range(y-1, y+2):
        for x2 in range(x-1, x+2):
            if (y2, x2) <= skip_until:
                continue

            if grid[y2][x2].isdigit():
                _, end, number = extract(x2, y2)
                numbers.append(number)
                skip_until = (y2, end)

    if len(numbers) == 2:
        return numbers[0] * numbers[1]

    return 0


result = 0

for y in range(1, n+1):
    for x in range(1, m+1):
        number = extract_ratio(x, y)
        result += number

submit(result, 2, 3, 2023)
