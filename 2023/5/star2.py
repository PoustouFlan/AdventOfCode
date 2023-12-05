import sys
sys.path.insert(0, "../../lib")
from aoc import submit

from typing import List, Tuple

def process_section(seeds: List[Tuple[int, int]]):
    """
    Reads a section, and applies all maps from the section to the input
    seed-interval list.
    Returns the new seed-interval list.
    """
    result_seeds = []       # Final result
    remaining_seeds = seeds # Numbers that have not yet been mapped

    done = False
    while not done:
        try:
            destination, source, length = map(int, input().split())
            delta = destination - source
            end = source + length # `end` is always excluded from a range

            # All seeds from the input will either go to
            # - result_seeds, if we know where the are mapped to
            # - remaining_seeds, otherwise

            remaining_seeds = []
            for start, stop in seeds:
                # (source, end(  denotes the range of seeds that the current map
                #                applies to
                # (start, stop(  denotes the current seed interval we are trying
                #                to map
                if source <= start < stop <= end:
                    # Seed interval is fully included in range
                    result_seeds.append((start + delta, stop + delta))

                elif start < source < stop <= end:
                    # Seed interval is partly included in range
                    remaining_seeds.append((start, source))
                    result_seeds.append((source + delta, stop + delta))

                elif source <= start < end < stop:
                    # Seed interval is partly included in range
                    result_seeds.append((start + delta, end + delta))
                    remaining_seeds.append((end, stop))

                elif start < source <= end < stop:
                    # Seed interval is partly included in range
                    remaining_seeds.append((start, source))
                    result_seeds.append((source + delta, end + delta))
                    remaining_seeds.append((end, stop))

                else:
                    # Seed interval is not included in range at all
                    remaining_seeds.append((start, stop))

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

# Read seed intervals

# seeds is now an array of intervals (start, end(
# (end is always excluded from an interval)
first_line_numbers = list(map(int, input().split()[1:]))

seeds = []
for i in range(0, len(first_line_numbers), 2):
    start = first_line_numbers[i]
    length = first_line_numbers[i + 1]
    seeds.append((start, start + length))

input()

# Process category convertions
done = False
while not done:
    try:
        line = input()
        seeds = process_section(seeds)

    except EOFError:
        done = True

submit(min(seeds)[0], 2, 5, 2023)
