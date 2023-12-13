import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Reading input
grids = []
grid = []
done = False
while not done:
    try:
        line = input()
        if line == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(line)

    except EOFError:
        # End of input
        done = True
        grids.append(grid)

def count_diff(line1, line2):
    """
    Returns the number of different characters between
    line1 and line2
    """
    diff = 0
    for char1, char2 in zip(line1, line2):
        if char1 != char2:
            diff += 1
    return diff

## Counting reflections
result = 0
for grid in grids:
    n = len(grid)
    m = len(grid[0])

    reflection_x = 0
    for x in range(1, m):
        # We check if there is a reflection between
        # column x - 1 and x
        diff = 0
        for i in range(min(x, m - x)):
            x1 = x - i - 1
            x2 = x + i

            # We extract the two columns
            line1 = [grid[y][x1] for y in range(n)]
            line2 = [grid[y][x2] for y in range(n)]

            diff += count_diff(line1, line2)
            if diff > 1:
                break

        if diff == 1:
            # It is a valid reflection
            reflection_x = x
            break

    reflection_y = 0
    for y in range(1, n):
        # We check if there is a reflection between
        # row y - 1 and y
        diff = 0
        for i in range(min(y, n - y)):
            y1 = y - i - 1
            y2 = y + i

            diff += count_diff(grid[y1], grid[y2])
            if diff > 1:
                break

        if diff == 1:
            # It is a valid reflection
            reflection_y = y
            break

    result += reflection_x
    result += 100 * reflection_y

submit(result, 2, 13, 2023)
