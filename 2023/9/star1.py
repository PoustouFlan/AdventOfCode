import sys
sys.path.insert(0, "../../lib")
from aoc import submit

result = 0

done = False
while not done:
    try:
        # Reading Input
        line = list(map(int, input().split()))

        while any(x != 0 for x in line):
            # Compute the difference table of the line
            for i in range(len(line) - 1):
                line[i] = line[i + 1] - line[i]

            # We add the last element of the row to the total result
            result += line.pop()

    except EOFError:
        # End of Input
        done = True

submit(result, 1, 9, 2023)
