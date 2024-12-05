import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # text = f.read()
    lines = f.read().split("\n")

ret = 0

rules = []
orders = []

flag = True
for l in lines:
    # print(l)
    if l == "":
        flag = False
        continue
    if flag:
        rules.append(list(map(int, l.split("|"))))
    else:
        orders.append(list(map(int, l.split(","))))

# print(rules)
# print(orders)

d = defaultdict(list)

for rule in rules:
    d[rule[0]].append(rule[1])

tmp = []
for o in orders:
    flag = True
    for i in range(len(o)):
        for j in range(i + 1, len(o)):
            if o[j] not in d[o[i]]:
                flag = False
                break
    if not flag:
        tmp.append(o)

# print(tmp)

for t in tmp:
    newt1 = t[::]
    newt = [newt1.pop()]

    while newt1:
        curr = newt1.pop()
        for i in range(len(newt)):
            if newt[i] in d[curr]:
                newt.insert(i, curr)
                break
        else:
            newt.append(curr)

    # print(len(newt), len(t))
    # print(newt)
    ret += newt[len(t) // 2]

print(ret)
