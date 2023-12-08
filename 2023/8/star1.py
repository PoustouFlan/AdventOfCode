import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from itertools import cycle

## Reading Input
directions = input()
input()

left_of = {}  # Map from a node to its left node
right_of = {} # Map from a node to its right node

res = 0
done = False
while not done:
    try:
        source, dest = input().split(' = ')
        left, right = dest.split(', ')
        left = left[1:]    # Trim the '('
        right = right[:-1] # Trim the ')'

        left_of[source] = left
        right_of[source] = right

    except EOFError:
        # End of Input
        done = True

## Main Computations
node = 'AAA'
steps = 0

# cycle through directions and count the steps
for direction in cycle(directions):
    if node == 'ZZZ':
        break

    steps += 1
    if direction == 'L':
        node = left_of[node]
    else:
        node = right_of[node]

submit(steps, 1, 8, 2023)
