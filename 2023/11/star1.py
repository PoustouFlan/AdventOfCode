import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Reading Input
grid = []

res = 0
done = False
while not done:
    try:
        line = list(input())
        grid.append(line)
    except EOFError:
        # End of Input
        done = True

## Input Preprocessing
N = len(grid)
M = len(grid[0])

is_row_empty = [True] * M
is_col_empty = [True] * N
galaxies = []

for y in range(N):
    for x in range(M):
        if grid[y][x] == '#':
            galaxies.append((x, y))
            is_row_empty[y] = False
            is_col_empty[x] = False

## Solving
total_distance = 0
for i, (xi, yi) in enumerate(galaxies):
    for xj, yj in galaxies[i + 1:]:
        x1, y1 = min(xi, xj), min(yi, yj)
        x2, y2 = max(xi, xj), max(yi, yj)

        for x in range(x1, x2):
            if is_col_empty[x]:
                total_distance += 2
            else:
                total_distance += 1

        for y in range(y1, y2):
            if is_row_empty[y]:
                total_distance += 2
            else:
                total_distance += 1


submit(total_distance, 1, 11, 2023)
