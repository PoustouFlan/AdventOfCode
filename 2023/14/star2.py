import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Reading input
grid = []
done = False
while not done:
    try:
        # Left and right sentinels
        line = '#' + input() + '#'
        grid.append(list(line))

    except EOFError:
        # End of input
        done = True

# The grid is a square grid.
# We lose a bit of generality to rotate the grid in-place later
n = len(grid[0])

# Top and bottom sentinels
sentinel = ['#'] * n
grid = [sentinel] + grid + [sentinel]

def roll_north():
    """
    Roll all the rocks upwards, in place
    """
    for x in range(n):
        # 2-pointers algorithm, O(n) amortized
        y_source = 0
        for y_dest in range(n):
            y_source = max(y_source, y_dest)

            # We attempt to find what element should we put onto y_dest
            while grid[y_dest][x] == '.' and grid[y_source][x] != '#':
                if grid[y_source][x] == 'O':
                    # Move the rock to the top
                    grid[y_dest][x] = 'O'
                    grid[y_source][x] = '.'
                y_source += 1

def rotate():
    """
    Rotate the grid 90 degrees clockwise, in place
    """
    # Transpose
    for y in range(n):
        for x in range(y, n):
            grid[y][x], grid[x][y] = grid[x][y], grid[y][x]

    # Swap columns
    for x in range(n // 2):
        for y in range(n):
            grid[y][x], grid[y][n - x - 1] = grid[y][n - x - 1], grid[y][x]

def spin_cycle():
    for _ in range(4):
        roll_north()
        rotate()

def grid_hash():
    result = 0
    for y, line in enumerate(grid):
        result ^= hash((y, ''.join(line)))
    return result

## Spin cycle until a loop is found
i = 0
known_states = {}
actual_hash = grid_hash()
while actual_hash not in known_states:
    known_states[actual_hash] = i
    spin_cycle()
    actual_hash = grid_hash()
    i += 1

## We can reduce the problem modulo the length of the loop
loop_length = known_states[actual_hash] - i
while (1000000000 - i) % loop_length != 0:
    spin_cycle()
    i += 1

## Load counting
total_load = 0
for y, line in enumerate(grid):
    total_load += line.count('O') * (n - y - 1)

submit(total_load, 2, 14, 2023)
