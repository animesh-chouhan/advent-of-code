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

for i, line in enumerate(lines):
    if line == row_dot:
        rows_added.append(i)

print(rows_added)

cols_added = []
for j in range(len(lines[0])):
    flag = True
    for i in range(len(lines)):
        if lines[i][j] == "#":
            flag = False
    if flag:
        cols_added.append(j)


print(cols_added)

points = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            points.append((i, j))

distance = []
print(points)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        print(points[i], points[j])
        d = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
        for r in rows_added:
            if points[i][0] < r < points[j][0] or points[j][0] < r < points[i][0]:
                d += 1000000 - 1
        for c in cols_added:
            if points[i][1] < c < points[j][1] or points[j][1] < c < points[i][1]:
                d += 1000000 - 1
        print(d)
        distance.append(d)

print(sum(distance))

print(f"Time taken: {time.time() - start_time}")
