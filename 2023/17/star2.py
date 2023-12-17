import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from heapq import *

## Constants
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

# Opposite directions can be obtained using XOR 1:
# 0 — 1 | NORTH — SOUTH
# 2 — 3 | EAST — WEST
DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

## Reading input
grid = []
done = False
while not done:
    try:
        line = list(input())
        grid.append(list(map(int, line)))

    except EOFError:
        # End of input
        done = True

## Processing
height = len(grid)
width = len(grid[0])
min_heat_loss = [
    [ [float('inf')] * 4 for _ in range(width) ]
    for _ in range(height)
]
# min_heat_loss[y][x][dir_index] = min heat loss at (x, y) while
# not being able to continue toward DIRS[dir_index]
# (probably because it was the last move)

# Dijkstra's algorithm
# Heap stores (heat loss, x, y, last direction)
heap = []
for dir_index in range(4):
    heappush(heap, (0, 0, 0, dir_index))

# Dijkstra's algorithm
while len(heap) > 0:
    heat_loss, x, y, forbidden_dir = heappop(heap)
    if min_heat_loss[y][x][forbidden_dir] <= heat_loss:
        # outdated value
        continue
    min_heat_loss[y][x][forbidden_dir] = heat_loss

    # Vertex processing
    for dir_index in range(4):
        # Recover heat_loss value
        heat_loss = min_heat_loss[y][x][forbidden_dir]

        # We cannot continue toward the same direction,
        # nor in the opposite direction.
        if dir_index == forbidden_dir or dir_index == forbidden_dir ^ 1:
            continue

        dx, dy = DIRECTIONS[dir_index]
        for move in range(1, 11):
            rx = x + move * dx
            ry = y + move * dy
            if not (0 <= rx < width and 0 <= ry < height):
                # Out of bounds
                break

            heat_loss += grid[ry][rx]

            # Minimal displacement of 4
            if move <= 3:
                continue

            heappush(heap, (heat_loss, rx, ry, dir_index))

submit(min(min_heat_loss[-1][-1]), 2, 17, 2023)
