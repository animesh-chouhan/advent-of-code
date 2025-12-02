import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split(",")

ret = 0
for l in lines:
    start, end = map(int, l.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        if s[: len(s) // 2] * 2 == s:
            ret += i

print(ret)
