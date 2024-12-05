from collections import defaultdict
from functools import cmp_to_key

rules, orders = open("input.txt").read().split("\n\n")
rules = [list(map(int, r.split("|"))) for r in rules.split("\n")]
orders = [list(map(int, o.split(","))) for o in orders.split("\n")]


d = defaultdict(set)
for rule in rules:
    d[rule[0]].add(rule[1])

ret = 0
for o in orders:
    s = sorted(o, key=cmp_to_key(lambda x, y: -1 if y in d[x] else 1))
    if o != s:
        ret += s[len(s) // 2]

print(ret)
