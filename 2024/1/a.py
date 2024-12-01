import pathlib

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

l1.sort()
l2.sort()

ret = 0
for a, b in zip(l1, l2):
    ret += abs(a - b)

print(ret)

# print(sum(abs(a - b) for a, b in zip(*[sorted(x) for x in zip(*[map(int, line.split()) for line in lines])])))
print(
    sum(
        abs(a - b)
        for a, b in zip(
            *[sorted(x) for x in zip(*[map(int, line.split()) for line in lines])]
        )
    )
)
