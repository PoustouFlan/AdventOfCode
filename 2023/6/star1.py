import sys
sys.path.insert(0, "../../lib")
from aoc import submit

# Input
times = list(map(int, input().split()[1:]))
distances = list(map(int, input().split()[1:]))

# Main computations
result = 1
for time, min_distance in zip(times, distances):
    possibilities = 0
    for i in range(time):
        distance = (time - i) * i
        if distance > min_distance:
            possibilities += 1

    result *= possibilities

submit(result, 1, 6, 2023)
