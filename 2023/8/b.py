import re
import time
import pathlib
import math

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


def get_steps(next_node):
    steps = 0
    found = False
    while not found:
        for i in instructions:
            if i == "L":
                next_node = nodes[next_node][0]
            elif i == "R":
                next_node = nodes[next_node][1]

            steps += 1
            print(steps, i, next_node)
            if next_node[2] == "Z":
                found = True
                break

    return steps


steps_list = []
nodes_a = [node for node in nodes if node[2] == "A"]
for node in nodes_a:
    steps_list.append(get_steps(node))


print(steps_list)
print(math.lcm(*steps_list))
print(f"Time taken: {time.time() - start_time}")
