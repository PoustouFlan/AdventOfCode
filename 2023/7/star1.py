import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from collections import Counter

# Relative order of cards
order = [
    '2', '3', '4', '5', '6', '7', '8', '9', 'T',
    'J', 'Q', 'K', 'A'
]

# Relative order of games, depending on card occurences
strength = [
    [1, 1, 1, 1, 1], # High card
    [1, 1, 1, 2],    # One pair
    [1, 2, 2],       # Two pairs
    [1, 1, 3],       # Three of a kind
    [2, 3],          # Full house
    [1, 4],          # Four of a kind
    [5]              # Five of a kind
]

def score(cards):
    """
    Returns the score of a hand, which is a tuple (kind, relative),
    where
    - kind is the kind of hand, going from 0 (high card) to 6 (five of a kind)
    - relative is a 5-tuple containing the relative orders of the cards,
      ranging from 0 ('2') to 12 ('A')

    This function can be used as a sorting key to sort hands based on strength
    """

    relative = tuple(order.index(x) for x in cards)
    counter = list(sorted(Counter(relative).values()))
    kind = strength.index(counter)
    return (kind, relative)


# Reading Input
done = False

hands = []
while not done:
    try:
        cards, bid = input().split()
        bid = int(bid)
        hands.append((cards, bid))
    except EOFError:
        done = True

# Sorting the hands by increasing strength
hands.sort(key = lambda hand: score(hand[0]))

# Computing the total winnings
result = 0
for i, (_, bid) in enumerate(hands):
    result += (i + 1) * bid

submit(result, 1, 7, 2023)
