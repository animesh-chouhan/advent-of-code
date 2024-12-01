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
row_dot = "." * len(lines[0])
rows_added = []

for line in lines:
    if line == row_dot:
        rows_added.append(row_dot)
    rows_added.append(line)

# for line in rows_added:
#     print(line)

cols_added = [[] for _ in rows_added]
for j in range(len(rows_added[0])):
    flag = True
    for i in range(len(rows_added)):
        cols_added[i].append(rows_added[i][j])
        if rows_added[i][j] == "#":
            flag = False
    if flag:
        for i in range(len(rows_added)):
            cols_added[i].append(".")


# for line in cols_added:
#     print(line)

points = []
for i in range(len(cols_added)):
    for j in range(len(cols_added[0])):
        if cols_added[i][j] == "#":
            points.append((i, j))

distance = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        print(points[i], points[j])
        distance.append(
            abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
        )

print(sum(distance))

print(f"Time taken: {time.time() - start_time}")
