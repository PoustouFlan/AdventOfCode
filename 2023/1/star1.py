import sys
sys.path.insert(0, "../../lib")
from aoc import submit

done = False
digits = [
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
]
result = 0
while not done:
    try:
        line = input()
        number = ''

        ## Reading first digit
        for char in line:
            if char.isdigit():
                number += char
                break

        ## Reading last digit
        for char in reversed(line):
            if char.isdigit():
                number += char
                break

        result += int(number)

    except EOFError:
        ## End of input
        done = True

submit(result, 1, 1, 2023)
