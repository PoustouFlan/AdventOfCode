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
        while len(number) == 0:
            for i in range(10):
                if line[0] == str(i) or line.startswith(digits[i]):
                    number += str(i)
                    break
            else:
                line = line[1:]

        ## Reading last digit
        while len(number) == 1:
            for i in range(10):
                if line[-1] == str(i) or line.endswith(digits[i]):
                    number += str(i)
                    break
            else:
                line = line[:-1]

        result += int(number)

    except EOFError:
        ## End of input
        done = True

submit(result, 2, 1, 2023)
