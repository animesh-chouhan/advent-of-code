import pathlib
from collections import Counter

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

l1 = []
l2 = []

for l in lines:
    a, b = map(int, l.split())
    l1.append(a)
    l2.append(b)

c = Counter(l2)
ret = 0
for e in l1:
    ret += e * c[e]

print(ret)

# print(sum(e * Counter(map(int, (l.split()[1] for l in lines)))[e] for e in map(int, (l.split()[0] for l in lines))))
print(
    sum(
        e * Counter(map(int, (l.split()[1] for l in lines)))[e]
        for e in map(int, (l.split()[0] for l in lines))
    )
)
