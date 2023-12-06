import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from math import isqrt

# Input
time = int(input().replace(' ', '').split(':')[1])
distance = int(input().replace(' ', '').split(':')[1])

# Main computations

#   (time - x) * x > distance
# ⇒ -x² + time*x - distance > 0
# ⇒ Quadratic equation
a = -1
b = time
c = -distance

delta = b*b - 4*a*c
x1 = (-b - isqrt(delta)) // (2*a)
x2 = (-b + isqrt(delta)) // (2*a)
# All hold time between x2 and x1 will beat the record

submit(x1 - x2, 2, 6, 2023)
