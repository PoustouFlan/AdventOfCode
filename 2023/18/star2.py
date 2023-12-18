import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Constants
EAST = (1, 0)
WEST = (-1, 0)
NORTH = (0, -1)
SOUTH = (0, 1)

DIRECTIONS = {
    '0': EAST,
    '1': SOUTH,
    '2': WEST,
    '3': NORTH,
}

## Reading input
x = y = 0
corners = [(x, y)] # List of all corners positions of the lagoon
x_values = {0}     # Set of all possible x coordinates for a corner
y_values = {0}     # Set of all possible y coordinates for a corner

done = False
while not done:
    try:
        _, _, color = input().split()
        direction = color[7]
        move = int(color[2:7], 16)

        dx, dy = DIRECTIONS[direction]

        x += move * dx
        y += move * dy
        corners.append((x, y))
        x_values.add(x)
        y_values.add(y)

    except EOFError:
        # End of input
        done = True

## Grid reduction
# Sort the x/y values
x_values = list(x_values)
y_values = list(y_values)
x_values.sort()
y_values.sort()

# We will make a bijection between original x/y coordinates and
# their position in the sorted x/y_values arrays
for i, (x, y) in enumerate(corners):
    # Grid is still expanded (x → 2 * x + 1)
    #     (see: my day 10 solution)
    x_reduced = 2 * x_values.index(x) + 1
    y_reduced = 2 * y_values.index(y) + 1
    corners[i] = (x_reduced, y_reduced)

# Reconstruction of the grid
height = len(y_values) * 2 + 2
width = len(x_values) * 2 + 2

grid = [[' '] * width for _ in range(height)]
x1, y1 = corners[0]
for x2, y2 in corners[1:]:
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x] = '#'
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

# Mark the right/bottom borders as of width 1 using sentinels
y_values.append(y_values[-1] + 1)
x_values.append(x_values[-1] + 1)

## Area measuring
capacity = 0
for y in range(1, height, 2):
    for x in range(1, width, 2):
        if grid[y][x] != '.':
            cell_height = y_values[y // 2 + 1] - y_values[y // 2]
            cell_width = x_values[x // 2 + 1] - x_values[x // 2]
            area = 1
            if grid[y+1][x+1] == ' ':
                # Tile is a full square
                area = cell_width * cell_height
            else:
                if grid[y+1][x] == '#':
                    # Tile contains a vertical wall
                    area += cell_height - 1
                if grid[y][x+1] == '#':
                    # Tile contains an horizontal wall
                    area += cell_width - 1
            
            capacity += area

submit(capacity, 2, 18, 2023)
