import sys
sys.path.insert(0, "../../lib")
from aoc import submit

result = 0
done = False
while not done:
    try:
        # Read input
        line = input().split(':')[1]
        winning, yours = line.split(' | ')
        winning = list(map(int, winning.split()))
        yours = list(map(int, yours.split()))

        # Compute points
        points = 1
        for elt in yours:
            if elt in winning:
                points *= 2

        result += (points // 2)

    except EOFError:
        # End of input
        done = True

submit(result, 1, 4, 2023)
