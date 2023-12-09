import re
import math
import time
import pathlib
from functools import reduce

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()


times = [int("".join(lines[0].split(":")[1].split()))]
distance = [int("".join(lines[1].split(":")[1].split()))]

# print(times)
# print(distance)

total = []
for i, t in enumerate(times):
    winning_distance = distance[i]
    det = math.sqrt(t * t - 4 * winning_distance)
    lower_root = (t - det) / 2
    upper_root = (t + det) / 2

    # print(lower_root, upper_root)
    wins = math.ceil(upper_root - 1) - math.floor(lower_root + 1) + 1
    total.append(wins)


# print(total)
print(reduce(lambda x, y: x * y, total))
print(f"Time taken: {time.time() - start_time}")
