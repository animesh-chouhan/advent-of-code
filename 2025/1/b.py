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
        if s != 0 and s - n <= 0:
            ret += 1
            ret += (n - s) // 100
            print(l)
        s -= n
    else:
        if s != 0 and s + n >= 100:
            ret += 1
            ret += (n + s - 100) // 100
        s += n

    s %= 100

print(ret)
