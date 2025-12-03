import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0

for l in lines:
    val = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            val = max(val, int(l[i] + l[j]))

    ret += val


print(ret)
