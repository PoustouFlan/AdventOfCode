import sys
sys.path.insert(0, "../../lib")
from aoc import submit

def hash(string):
    """
    HASH algorithm
    """
    result = 0
    for char in string:
        result += ord(char)
        result *= 17
        result %= 256
    return result

## Main 
boxes = [[] for _ in range(256)]

for step in input().split(','):
    # Read step
    if '=' in step:
        separator = '='
    else:
        separator = '-'

    key, focal_length = step.split(separator)
    box_index = hash(key)

    if separator == '=':
        # Add the value to the HASHMAP
        focal_length = int(focal_length)
        for i, (old_key, _) in enumerate(boxes[box_index]):
            if old_key == key:
                # Replace the lens that is already present
                boxes[box_index][i] = (key, focal_length)
                break
        else:
            boxes[box_index].append((key, focal_length))

    else:
        # Remove the focal_length of the HASHMAP
        for i, (old_key, _) in enumerate(boxes[box_index]):
            if old_key == key:
                # Delete the lens that is already present
                boxes[box_index].pop(i)
                break

# Computing focusing power
power = 0
for box_number in range(256):
    for slot_number, (_, focal_length) in enumerate(boxes[box_number]):
        power += (box_number + 1) * (slot_number + 1) * focal_length

submit(power, 2, 15, 2023)
