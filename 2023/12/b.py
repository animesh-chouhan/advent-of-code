import re
import time
import copy
import pathlib

from pigeonhole import pigeonhole


input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()
arrangement = []

springs = [line.split()[0] for line in lines]
broken_springs = [list(map(int, line.split()[1].split(","))) for line in lines]

# print(springs)
# print(broken_springs)
springs = ["?".join([spring] * 5) for spring in springs]
broken_springs = [b * 5 for b in broken_springs]


def compare(spring, temp_string):
    flag = True
    for i in range(len(spring)):
        if spring[i] != temp_string[i] and spring[i] != "?":
            return 0
    return 1


for i, spring in enumerate(springs):
    print(spring)
    total_len = len(spring)
    spring_len = sum(broken_springs[i])
    sep_len = total_len - spring_len
    # print(sep_len)
    spring_list = ["#" * s for s in broken_springs[i]]
    # print(spring_list)
    min_sep_usage = len(spring_list) - 1
    sep_left = sep_len - min_sep_usage
    # print(sep_left)
    # print(".".join(spring_list))

    if sep_left == 0:
        arrangement.append(1)
        continue

    sep_list = [1 for _ in range(len(spring_list) - 1)]
    sep_list.append(0)
    sep_list.insert(0, 0)
    # print(sep_list)

    possible = list(pigeonhole(sep_left, len(sep_list)))
    count = 0
    for p in possible:
        temp_string = ""
        for j in range(len(p) - 1):
            temp_string += "." * (sep_list[j] + p[j])
            temp_string += spring_list[j]
        temp_string += "." * (sep_list[-1] + p[-1])
        # print(temp_string)
        count += compare(spring, temp_string)

    print(count)
    arrangement.append(count)

print(sum(arrangement))

print(f"Time taken: {time.time() - start_time}")
