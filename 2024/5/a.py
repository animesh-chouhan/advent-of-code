import pathlib
from collections import defaultdict
from functools import cmp_to_key

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    text = f.read()
    # lines = f.read().split("\n")

ret = 0

rules, orders = text.split("\n\n")
rules = [list(map(int, r.split("|"))) for r in rules.split("\n")]
orders = [list(map(int, o.split(","))) for o in orders.split("\n")]


d = defaultdict(set)
for rule in rules:
    d[rule[0]].add(rule[1])


def compare(x, y):
    if y in d[x]:
        return -1
    return 1


for o in orders:
    if o == sorted(o, key=cmp_to_key(compare)):
        ret += o[len(o) // 2]


print(ret)
