import sys
sys.path.insert(0, "../../lib")
from aoc import submit

## Classes and methods

def predicate_of(condition):
    """
    Returns a predicate from a rule's condition
    Example of condition:
        'x>10'
    """
    def predicate(**ratings):
        """
        Given the ratings of 'x', 'm', 'a' and 's',
        (given as keyword arguments)
        returns True if the corresponding rule should be applied
        """
        category = condition[0]
        rating = ratings[category]
        threshold = int(condition[2:])
        if condition[1] == '<':
            return rating < threshold
        else:
            return rating > threshold

    return predicate

def default_predicate(**kwargs):
    """
    Predicate for the default rule.
    Always returns True.
    """
    return True

class Workflow:
    """
    Represents a Workflow, a list of rules.
    Exemple of rules for __init__:
        'a<2006:qkq,m>2090:A,rfg'
    """
    def __init__(self, rules):
        rules = rules.split(',')

        # List of (predicate, next workflow if True)
        self.rules = []

        # Parsing all rules with condition
        for rule in rules[:-1]:
            condition, destination = rule.split(':')
            self.rules.append((predicate_of(condition), destination))

        # Parsing default rule
        self.rules.append((default_predicate, rules[-1]))

    def accepts(self, **ratings):
        """
        Given the values of 'x', 'm', 'a' and 's',
        (given as keyword arguments)
        Returns True if the workflow accepts the given parts
        """
        for condition, destination in self.rules:
            if condition(**ratings):
                if destination == 'A':
                    return True
                if destination == 'R':
                    return False
                # Redirect to the correct workflow
                return workflows[destination].accepts(**ratings)

## Reading workflows
workflows = {}

while True:
    line = input()
    if line == '':
        break

    title, rules = line.split('{')
    rules = rules[:-1]
    workflows[title] = Workflow(rules)

## Reading parts
total_ratings = 0

done = False
while not done:
    try:
        line = input()[1:-1].split(',')

        # Parse ratings
        ratings = {}
        for part in line:
            category, rating = part.split('=')
            ratings[category] = int(rating)

        # Check acceptance
        if workflows['in'].accepts(**ratings):
            total_ratings += sum(ratings.values())

    except EOFError:
        # End of input
        done = True

submit(total_ratings, 1, 19, 2023)
