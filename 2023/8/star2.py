import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from itertools import cycle
from math import lcm

## Reading Input
directions = input()
input()

start_points = [] # List of starting nodes
left_of = {}  # Map from a node to its left node
right_of = {} # Map from a node to its right node

res = 0
done = False
while not done:
    try:
        source, dest = input().split(' = ')

        if source[-1] == 'A':
            start_points.append(source)

        left, right = dest.split(', ')
        left = left[1:]    # Trim the '('
        right = right[:-1] # Trim the ')'

        left_of[source] = left
        right_of[source] = right

    except EOFError:
        # End of Input
        done = True


## Main Computations
result = 1

for node in start_points:
    # Compute the expected cycle length starting from node
    steps = 0
    for direction in cycle(directions):
        if node[-1] == 'Z':
            break

        steps += 1
        if direction == 'L':
            node = left_of[node]
        else:
            node = right_of[node]

    # Result is the least common multiple of all the cycle lengths
    result = lcm(result, steps)

submit(result, 2, 8, 2023)
