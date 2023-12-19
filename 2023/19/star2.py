import sys
sys.path.insert(0, "../../lib")
from aoc import submit

class Predicate:
    """
    Represent a more complex kind of predicate that can handle combining
    with other predicates, and directly counting the number of accepting inputs

    Example of condition for __init__:
        x>10

    When negated is True, returns the opposite condition.
    """
    def __init__(self, condition = None, negated = False):
        # predicate is True if all variables lies in the corresponding intervals
        # As usual, the convention "lower bound included, upper bound excluded"
        # is used.
        self.intervals = {
            var: [1, 4001] for var in 'xmas'
        }

        if condition == None:
            return

        variable = condition[0]
        value = int(condition[2:])

        if negated:
            if condition[1] == '<': # ≥
                self.intervals[variable][0] = value
            else:                   # ≤
                self.intervals[variable][1] = value + 1
        else:
            if condition[1] == '<': # <
                self.intervals[variable][1] = value
            else:                   # >
                self.intervals[variable][0] = value + 1


    def __and__(self, other):
        """
        Returns a predicate that is True when both self AND other are True
        """
        result = Predicate()
        for var in 'xmas':
            min_v = max(self.intervals[var][0], other.intervals[var][0])
            max_v = min(self.intervals[var][1], other.intervals[var][1])
            result.intervals[var] = [min_v, max_v]
        return result


    def accepting_count(self):
        """
        Returns the number of ratings that fulfill this predicate
        """
        result = 1
        for min_v, max_v in self.intervals.values():
            result *= max_v - min_v
        return result


class Workflow:
    """
    Represents a Workflow, a list of rules.
    Exemple of rules for __init__:
        'a<2006:qkq,m>2090:A,rfg'
    """
    def __init__(self, rules):
        rules = rules.split(',')

        # List of (condition, next workflow if True)
        self.rules = []

        # Parsing all rules with condition
        # Condition for "All previous conditions are False"
        otherwise = Predicate()
        for rule in rules[:-1]:
            condition, destination = rule.split(':')
            predicate = Predicate(condition)
            negated_predicate = Predicate(condition, negated = True)

            # The actual condition is 
            # "This one, and none of the previous ones"
            self.rules.append((otherwise & predicate, destination))
            otherwise &= negated_predicate

        # Parsing default rule
        self.rules.append((otherwise, rules[-1]))


    def reduce(self):
        """
        A workflow is denoted 'reduced' when all of its rules directly leads
        to ACCEPT or REJECT, with no possible intermediate workflows.
        This method converts the workflow into a reduced form.
        """
        reduced_rules = []
        for predicate, destination in self.rules:
            if destination in ('A', 'R'):
                # Rule is already reduced
                reduced_rules.append((predicate, destination))
                continue

            destination_workflow = workflows[destination]
            destination_workflow.reduce()

            for sub_predicate, acceptance in destination_workflow.rules:
                # Acceptance may only be A or R, since destination_workflow
                # is reduced.
                reduced_rules.append((predicate & sub_predicate, acceptance))

        self.rules = reduced_rules


    def accepting_count(self):
        """
        Returns the number of ratings that are accepted by this workflow
        """
        self.reduce()

        count = 0
        for predicate, acceptance in self.rules:
            if acceptance == 'A':
                count += predicate.accepting_count()

        return count

## Reading workflows
workflows = {}

while True:
    line = input()
    if line == '':
        break

    title, rules = line.split('{')
    rules = rules[:-1]
    workflows[title] = Workflow(rules)

## Counting accepted ratings
accepted_ratings = workflows['in'].accepting_count()

submit(accepted_ratings, 2, 19, 2023)
