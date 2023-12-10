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

## Finding the correct replacement for S
directions = []
for dx, dy in adj:
    opposite = (-dx, -dy)
    rx, ry = sx + dx, sy + dy
    if opposite in pipes[grid[ry][rx]]:
        directions.append((dx, dy))
assert len(directions) > 0

for pipe, links in pipes.items():
    if (links == (directions[0], directions[1]) or
        links == (directions[1], directions[0])):
           grid[sy][sx] = pipe
           break
assert grid[sy][sx] != 'S'

direction = directions[0]

## Traversing the loop
loop = {(sx, sy)}
dx, dy = direction        # Current direction
x1, y1 = sx, sy           # Previous position
x2, y2 = x1 + dx, y1 + dy # Current position

while (x2, y2) != (sx, sy):
    loop.add((x2, y2))

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

## Removing every pipe that is not part of the loop
for y in range(N):
    for x in range(N):
        if (x, y) not in loop:
            grid[y][x] = '.'

## Expanding the input

#        #####
# F-7    #   #
# L7|  ⇒ ### #
#  LJ      # #
#          ###

expanded_grid = []
for line in grid:
    expanded_line1 = []
    expanded_line2 = []
    for pipe in line:
        if pipe != '.':
            expanded_line1.append('#')
        else:
            expanded_line1.append(' ')

        if EAST in pipes[pipe]:
            expanded_line1.append('#')
        else:
            expanded_line1.append(' ')
        if SOUTH in pipes[pipe]:
            expanded_line2.append('#')
        else:
            expanded_line2.append(' ')

        expanded_line2.append(' ')
    expanded_grid.append(expanded_line1)
    expanded_grid.append(expanded_line2)

## Filling the outsides

# #####   #####
# #   #   #   #
# ### # ⇒ ### #
#   # #   ### #
#   ###   #####

level = [(0, 0)] # (0, 0) is always a blank outside, thanks to the sentinel
expanded_grid[0][0] = '#'

# level-order traversal (BFS)
while len(level) > 0:
    next_level = []
    for x, y in level:
        for dx, dy in adj:
            rx, ry = x + dx, y + dy
            if expanded_grid[ry][rx] == ' ':
                expanded_grid[ry][rx] = '#'
                next_level.append((rx, ry))

    level = next_level

## Counting the insides
result = 0

# Original pipes have even x/y coordinates in expanded grid
for x in range(0, 2 * N, 2):
    for y in range(0, 2 * N, 2):
        if expanded_grid[y][x] == ' ':
            result += 1

submit(result, 2, 10, 2023)
