import re
import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n\n")


# print(lines)
def find(r, s):
    return int(re.search(r, s).group(1))


tokens = 0
for line in lines:
    a, b, p = line.split("\n")
    a = find(r"X\+(\d+)", a), find(r"Y\+(\d+)", a)
    b = find(r"X\+(\d+)", b), find(r"Y\+(\d+)", b)
    p = 10000000000000 + find(r"X\=(\d+)", p), 10000000000000 + find(r"Y\=(\d+)", p)
    # print(a, b, p)

    # ax, by
    # a[0] * x + b[0] * y = p[0]
    # a[1] * x + b[1] * y = p[1]

    d = a[0] * b[1] - a[1] * b[0]
    if d != 0:
        x = (p[0] * b[1] - p[1] * b[0]) / d
        y = (p[1] * a[0] - p[0] * a[1]) / d
        # print(x, y)
        if x.is_integer() and y.is_integer() and x >= 0 and y >= 0:
            tokens += 3 * x + y
    else:
        if a[0] * p[1] == a[1] * p[0]:
            print("yay")
            tokens += 1

print(tokens)
