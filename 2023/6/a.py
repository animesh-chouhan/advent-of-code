import re
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


times = list(map(int, lines[0].split(":")[1].split()))
distance = list(map(int, lines[1].split(":")[1].split()))

# print(times)
# print(distance)

total = []
for i, t in enumerate(times):
    possible_distances = []
    winning_distance = distance[i]
    for j in range(t):
        charge_time = j
        left_time = t - j
        if charge_time == 0 or left_time == 0:
            continue
        possible_distances.append(charge_time * left_time)

    # print(possible_distances)
    wins = [d for d in possible_distances if d > winning_distance]
    total.append(len(wins))


# print(total)
print(reduce(lambda x, y: x * y, total))
print(f"Time taken: {time.time() - start_time}")
