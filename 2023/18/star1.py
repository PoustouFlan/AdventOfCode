import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Constants
EAST = (1, 0)
WEST = (-1, 0)
NORTH = (0, -1)
SOUTH = (0, 1)

DIRECTIONS = {
    'R': EAST,
    'D': SOUTH,
    'L': WEST,
    'U': NORTH,
}

## Reading input
x = y = 0
corners = [(x, y)]
min_x = max_x = 0
min_y = max_y = 0

done = False
while not done:
    try:
        direction, move, _ = input().split()
        move = int(move)
        dx, dy = DIRECTIONS[direction]

        # Grid is expanded for interior detection
        #     (see: my day 10 solution)
        x += 2 * move * dx
        y += 2 * move * dy
        corners.append((x, y))

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    except EOFError:
        # End of input
        done = True

## Grid creation
height = max_y - min_y + 3
width = max_x - min_x + 3
grid = [[' '] * width for _ in range(height)]

x1, y1 = corners[0]
for x2, y2 in corners[1:]:
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y - min_y + 1][x - min_x + 1] = '#'
    x1, y1 = x2, y2

## Inside/outside segmentation

# Level-order BFS to mark the outside
level = [(0, 0)]
while len(level) > 0:
    next_level = []

    # Level processing
    for x, y in level:
        for dx, dy in DIRECTIONS.values():
            rx = x + dx
            ry = y + dy
            if not (0 <= rx < width and 0 <= ry < height):
                # Out of bounds
                continue
            
            # Vertex processing
            if grid[ry][rx] == ' ':
                grid[ry][rx] = '.'
                next_level.append((rx, ry))
    level = next_level

## Counting the insides
capacity = 0
for y in range(1, height, 2):
    for x in range(1, width, 2):
        if grid[y][x] != '.':
            capacity += 1

submit(capacity, 1, 18, 2023)
