import sys
sys.path.insert(0, "/home/poustouflan/CP/AdventOfCode/lib")
from aoc import submit

done = False
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
res = 0
while not done:
    try:
        line = input()
        n = ''

        ## Lecture du premier chiffre
        while len(n) == 0:
            for x in range(10):
                if line[0] == str(x) or line.startswith(digits[x]):
                    n += str(x)
                    break
            else:
                line = line[1:]

        ## Lecture du dernier chiffre
        while len(n) == 1:
            for x in range(10):
                if line[-1] == str(x) or line.endswith(digits[x]):
                    n += str(x)
                    break
            else:
                line = line[:-1]
        res += int(n)

    except EOFError:
        ## Fin de l'entrée
        done = True

submit(res, 2)
