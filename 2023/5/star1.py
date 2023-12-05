import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from typing import List, Tuple

def process_section(seeds: List[int]):
    """
    Reads a section, and applies all maps from the section to the input seed
    list.
    Returns the new seed list.
    """

    result_seeds = []       # Final result
    remaining_seeds = seeds # Numbers that have not yet been mapped

    done = False
    while not done:
        try:
            destination, source, length = map(int, input().split())
            end = source + length # `end` is always excluded from a range

            # All seeds from the input will either go to
            # - result_seeds, if we know where the are mapped to
            # - remaining_seeds, otherwise

            remaining_seeds = []
            for seed in seeds:
                if source <= seed < end:
                    # Expected displacement of the seed's value
                    delta = destination - source
                    result_seeds.append(seed + delta)
                else:
                    remaining_seeds.append(seed)

            # We continue to process the seeds that are not yet mapped.
            seeds = remaining_seeds

        # End of section
        except EOFError:
            done = True
        except ValueError:
            done = True

    # All source numbers that are not yet mapped stay the same
    result_seeds.extend(remaining_seeds)
    return result_seeds


## MAIN

# Read seed numbers
seeds = list(map(int, input().split()[1:]))
input()

# Process category convertions
done = False
while not done:
    try:
        line = input()
        seeds = process_section(seeds)

    except EOFError:
        done = True

submit(min(seeds), 1, 5, 2023)
