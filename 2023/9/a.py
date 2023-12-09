import re
import time
import pathlib
from functools import cmp_to_key
from collections import Counter

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()


instructions = lines[0]
nodes = {
    line.split(" = ")[0]: (
        line.split(" = ")[1][1:-1].split(", ")[0],
        line.split(" = ")[1][1:-1].split(", ")[1],
    )
    for line in lines[2:]
}

# print(instructions)
# print(nodes)

steps = 0
next_node = "AAA"
found = False
while not found:
    for i in instructions:
        if i == "L":
            next_node = nodes[next_node][0]
        elif i == "R":
            next_node = nodes[next_node][1]

        steps += 1
        print(steps, i, next_node)
        if next_node == "ZZZ":
            found = True
            break

print(steps)
print(f"Time taken: {time.time() - start_time}")
