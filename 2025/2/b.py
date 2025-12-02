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
        l = len(s)
        for j in range(l, 1, -1):
            if l % j == 0:
                if s[: l // j] * j == s:
                    ret += i
                    break

print(ret)
