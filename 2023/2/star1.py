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
        possible = True

        # Maximum number of cubes for each color
        available = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

        for game in games:
            game = game.split(', ')
            for cube in game:
                number, color = cube.split()
                number = int(number)
                if number > available[color]:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            result += id

    # End of input
    except EOFError:
        done = True

submit(result, 1, 2, 2023)
