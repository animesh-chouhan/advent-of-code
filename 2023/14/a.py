import re
import time
import copy
import pathlib


input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()

cols_count = len(lines[0])
cols = ["" for _ in range(cols_count)]
# print(cols)
for i in range(cols_count):
    for line in lines:
        cols[i] += line[i]

# for col in cols:
#     print(col)

splitted_col = [col.split("#") for col in cols]

transformed_cols = []
for col in splitted_col:
    temp = []
    for s in col:
        sorted_s = "".join(sorted(s, reverse=True))
        temp.append(sorted_s)
    transformed_cols.append("#".join(temp))

load = []
for col in transformed_cols:
    # print(col)
    for i in range(len(col)):
        if col[i] == "O":
            load.append(len(col) - i)

print(load)
print(sum(load))

print(f"Time taken: {time.time() - start_time}")
