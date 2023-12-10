import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## CONSTANTS

# Directions
NORTH = (0, -1)
SOUTH = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)

adj = (NORTH, SOUTH, WEST, EAST)

# Pipes
pipes = {
    '|': (NORTH, SOUTH),
    '-': (EAST, WEST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST),
    '.': (),
}

## Reading Input
grid = []
res = 0
done = False
while not done:
    try:
        # Add a border of '.' as a sentinel
        line = ['.'] + list(input()) + ['.']
        grid.append(line)

    except EOFError:
        # End of input
        done = True

extra = ['.'] * (len(grid[0]))
grid = [extra] + grid + [extra]

# Size of the (modified) input
N = len(grid)
M = len(grid[0])

## Finding 'S'
sx, sy = None, None
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'S':
            sx, sy = x, y
            break
    # break propagation
    if sx is not None:
        break

assert sx is not None and sy is not None

## Finding the direction to go from S
# A good direction is any direction in which the pipe located
# toward this direction points back toward the S.
direction = None
for dx, dy in adj:
    opposite = (-dx, -dy)
    rx, ry = sx + dx, sy + dy
    if opposite in pipes[grid[ry][rx]]:
        direction = (dx, dy)
        break

assert direction is not None

## Traversing the loop

dx, dy = direction        # Current direction
x1, y1 = sx, sy           # Previous position
x2, y2 = x1 + dx, y1 + dy # Current position

loop_size = 1
while (x2, y2) != (sx, sy):
    loop_size += 1

    # The correct direction is the one that is not the
    # opposite of our current direction
    opposite = (-dx, -dy)
    direction1, direction2 = pipes[grid[y2][x2]]
    if direction1 == opposite:
        direction = direction2
    else:
        direction = direction1

    # We move toward the correct direction
    dx, dy = direction
    x3, y3 = x2 + dx, y2 + dy
    x1, y1 = x2, y2
    x2, y2 = x3, y3

submit(loop_size // 2, 1, 10, 2023)
