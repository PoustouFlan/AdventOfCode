import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Reading input
grid = []
done = False
while not done:
    try:
        line = input()
        grid.append(list(line))

    except EOFError:
        # End of input
        done = True

height = len(grid)
width = len(grid[0])

# Sentinel
sentinel = ['#'] * width
grid.append(sentinel)

## Rolling rocks 
for x in range(width):
    # 2-pointers algorithm, O(height) amortized
    y_source = 0
    for y_dest in range(height):
        y_source = max(y_source, y_dest)

        # We attempt to find what element should we put onto y_dest
        while grid[y_dest][x] == '.' and grid[y_source][x] != '#':
            if grid[y_source][x] == 'O':
                # Move the rock to the top
                grid[y_dest][x] = 'O'
                grid[y_source][x] = '.'
            y_source += 1

## Load counting
total_load = 0
for y, line in enumerate(grid):
    total_load += line.count('O') * (height - y)

submit(total_load, 1, 14, 2023)
