import sys
sys.path.insert(0, "../../lib")
from aoc import submit

cards = [] # Card count queue
result = 0
done = False
while not done:
    try:
        # Read input
        line = input().split(':')[1]
        winning, yours = line.split(' | ')
        winning = list(map(int, winning.split()))
        yours = list(map(int, yours.split()))

        # Compute actual number of cards
        if len(cards) == 0:
            card_count = 1
        else:
            card_count = 1 + cards.pop(0)

        # Compute score
        result += card_count
        points = 0
        for elt in yours:
            if elt in winning:
                points += 1

        # Save new cards
        for i in range(points):
            if i >= len(cards):
                cards.append(card_count)
            else:
                cards[i] += card_count

    except EOFError:
        done = True

submit(result, 2, 4, 2023)
