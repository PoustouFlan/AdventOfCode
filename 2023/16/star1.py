import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Constants
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

DIRECTIONS = (NORTH, SOUTH, EAST, WEST)

# REFLECTION[tile content][beam direction]
# returns the list of new directions the beam must head toward
REFLECTION = {
    '.' : {
        NORTH: [NORTH],
        SOUTH: [SOUTH],
        EAST: [EAST],
        WEST: [WEST],
    },
    '-' : {
        NORTH: [EAST, WEST],
        SOUTH: [EAST, WEST],
        EAST: [EAST],
        WEST: [WEST],
    },
    '|' : {
        NORTH: [NORTH],
        SOUTH: [SOUTH],
        EAST: [NORTH, SOUTH],
        WEST: [NORTH, SOUTH],
    },
    '/' : {
        NORTH: [EAST],
        SOUTH: [WEST],
        EAST: [NORTH],
        WEST: [SOUTH],
    },
    '\\' : {
        NORTH: [WEST],
        SOUTH: [EAST],
        EAST: [SOUTH],
        WEST: [NORTH],
    },
}

## Reading input
grid = []
done = False
while not done:
    try:
        line = input()
        grid.append(line)

    except EOFError:
        # End of input
        done = True

height = len(grid)
width = len(grid[0])

## Launching the beam
# already[y][x][direction] = "Has any beam already entered tile (x, y) toward
# this direction previously?"
already = [
    [ { direction: False for direction in DIRECTIONS } for x in range(width) ]
    for y in range(height)
]

# starting beam
already[0][0][EAST] = True

# level-order breadth-first search
# (because Python is not very found of depth-first search)
level = [((0, 0), EAST)]

while len(level) > 0:
    next_level = []
    # Level processing
    for (x, y), direction in level:
        # Vertex processing
        for dx, dy in REFLECTION[grid[y][x]][direction]:
            # We make one step toward the new direction: (dx, dy)
            rx = x + dx
            ry = y + dy

            if not (0 <= rx < width and 0 <= ry < height):
                # Out of bound
                continue

            if already[ry][rx][(dx, dy)]:
                # We entered a cycle that has already been computed,
                # we can stop directly.
                continue

            already[ry][rx][(dx, dy)] = True
            next_level.append(((rx, ry), (dx, dy)))

    level = next_level

## Count the number of visited tiles
energized = 0
for y in range(height):
    for x in range(width):
        if any(visited for visited in already[y][x].values()):
            energized += 1

submit(energized, 1, 16, 2023)
