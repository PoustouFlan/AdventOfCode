import sys
sys.path.insert(0, "/home/poustouflan/CP/AdventOfCode/lib")
from aoc import submit

res = 0
done = False
while not done:
    try:
        line = input()

    except EOFError:
        done = True

print(res)
#submit(res)
