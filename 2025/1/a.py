import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0

s = 50

for l in lines:
    d = l[0]
    n = int(l[1:])
    if d == "L":
        s -= n
    else:
        s += n

    s %= 100
    if s == 0:
        ret += 1

print(ret)
