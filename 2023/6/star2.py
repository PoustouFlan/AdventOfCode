import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from math import isqrt

def ceil_sqrt(x):
    # Returns ceil(sqrt(x)) with only integer arithmetics.
    candidate = isqrt(x)
    if candidate * candidate == x:
        return candidate
    else:
        return candidate + 1

# Input
time = int(input().replace(' ', '').split(':')[1])
distance = int(input().replace(' ', '').split(':')[1])

# Main computations

#   (time - x) * x > distance
# ⇒ x² - time*x + distance > 0
# ⇒ Quadratic equation
a = 1
b = -time
c = distance

delta = b*b - 4*a*c
x1 = (-b - ceil_sqrt(delta)) // (2*a)             # Rounded down
x2 = (-b + ceil_sqrt(delta) + (2*a - 1)) // (2*a) # Rounded up

# All hold time between x1 and x2 will beat the record
# (both x1 and x2 are excluded)
# ⇒ x2 - x1 - 1 solutions

submit(x2 - x1 - 1, 2, 6, 2023)
