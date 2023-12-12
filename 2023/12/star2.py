import sys
sys.path.insert(0, "../../lib")
from aoc import submit

def solve(springs, groups):
    """
    Returns the number of consistent arrangements for the given list of springs
    """
    springs = '.' + springs + '.' # Sentinels
    n = len(springs)
    m = len(groups)

    # count_operational[i] = number of possibly operational springs up to
    #                        spring i (excluded)
    count_operational = [0]
    total = 0
    for spring in springs:
        if spring in '#?':
            total += 1
        count_operational.append(total)

    def may_be_a_group(start, length):
        """
        Returns True if springs[start : start+length] may be a valid group
        """
        # We must have a damaged spring at index i-1 and i + group_length,
        # and all springs from index i to index i + group_length (excluded)
        # must be operational.

        # The latter condition may be checked in O(1) using the prefix array
        # count_operational
        return (
            springs[start-1] != '#' and 
            count_operational[start + length] - count_operational[start] == length and
            springs[start + length] != '#'
        )

    # dp[i][j] = solve(springs[i:], groups[j:])
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    ## Base case
    # dp[i][m] = 1 if there are no damaged strings
    # starting from index i.
    dp[n][m] = 1
    for i in range(n - 1, -1, -1):
        if springs[i] == '#':
            break
        dp[i][m] = 1

    ## General case
    for j in range(m-1, -1, -1):
        group_length = groups[j]
        for i in range(n - group_length, 0, -1):
            # Try to consider the elements [i : i + group_length] as operational
            if may_be_a_group(i, group_length):
                dp[i][j] += dp[i + group_length + 1][j + 1]

            # Try to consider the element i as damaged
            if (springs[i] != '#'):
                dp[i][j] += dp[i + 1][j]

    return dp[1][0]

## Input parsing
result = 0
done = False
while not done:
    try:
        springs, groups = input().split()
        groups = list(map(int, groups.split(',')))

        springs = (springs + '?') * 4 + springs
        groups  = groups * 5

        result += solve(springs, groups)

    except EOFError:
        # End of input
        done = True

submit(result, 2, 12, 2023)
