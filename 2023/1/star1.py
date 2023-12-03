import sys
sys.path.insert(0, "../../lib")
from aoc import submit

done = False
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
res = 0
while not done:
    try:
        line = input()
        n = ''

        ## Lecture du premier chiffre
        for x in line:
            if x.isdigit():
                n += x
                break

        ## Lecture du dernier chiffre
        for x in reversed(line):
            if x.isdigit():
                n += x
                break

        res += int(n)

    except EOFError:
        ## Fin de l'entrée
        done = True

submit(res, 1, 1, 2023)
