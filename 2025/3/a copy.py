import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0

for l in lines:
    m = max(l)
    idx = l.find(m)
    if idx == len(l) - 1:
        m = max(l[:-1])
        idx = l.find(m)

    n = max(l[idx + 1 :])
    ret += int(m + n)


print(ret)
