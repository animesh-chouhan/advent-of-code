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


def get_value(sequence):
    # print(sequence)
    diff = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

    if set(diff) == {0}:
        return sequence[0]
    return sequence[0] - get_value(diff)


value_list = [list(map(int, line.split())) for line in lines]
# print(value_list)

next_value_list = [get_value(l) for l in value_list]
# print(next_value_list)
print(sum(next_value_list))

print(f"Time taken: {time.time() - start_time}")
