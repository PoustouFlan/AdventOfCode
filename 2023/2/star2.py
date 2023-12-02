import sys
sys.path.insert(0, "../../lib")
from aoc import submit

result = 0

done = False
while not done:
    try:
        id, games = input().split(': ')
        id = int(id.split()[1])
        games = games.split('; ')

        # Minimal number of cube needed for each color
        needed = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for game in games:
            game = game.split(', ')
            for cube in game:
                number, color = cube.split()
                number = int(number)
                needed[color] = max(needed[color], number)

        # Computation of the power of the set of cubes
        power = 1
        for number in needed.values():
            power *= number

        result += power

    # End of input
    except EOFError:
        done = True

submit(result, 2)
