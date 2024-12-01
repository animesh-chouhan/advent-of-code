import re
import time
import copy
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    patterns = [p.split("\n") for p in f.read().split("\n\n")]

# print(patterns)

vertical = []
horizontal = []
for pattern in patterns:
    pattern_col = len(pattern[0])
    for i in range(1, pattern_col):
        len_overlap = min(i, pattern_col - i)
        # print(len_overlap)
        left = [row[i - len_overlap : i] for row in pattern]
        right = [row[i : i + len_overlap][::-1] for row in pattern]

        # print(left, right)
        count = 0
        for l, r in zip(left, right):
            for c in range(len(r)):
                if l[c] != r[c]:
                    count += 1
        # print(count)
        if count == 1:
            # print(i)
            vertical.append(i)

    pattern_row = len(pattern)
    for j in range(1, pattern_row):
        len_overlap = min(j, pattern_row - j)
        # print(len_overlap)
        top = pattern[j - len_overlap : j]
        bottom = pattern[j : j + len_overlap][::-1]

        # print(top, bottom)
        count = 0
        for t, b in zip(top, bottom):
            for c in range(len(t)):
                if t[c] != b[c]:
                    count += 1

        if count == 1:
            # print(top, bottom)
            print(j)
            vertical.append(j * 100)

print(sum(vertical) + sum(horizontal))

start_time = time.time()


print(f"Time taken: {time.time() - start_time}")
