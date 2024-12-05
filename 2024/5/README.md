# Day 5

https://adventofcode.com/2024/day/5

## Data format

The input contains both rules and evaluation patterns.

### Part A

> _What do you get if you add up the middle page number from those correctly-ordered updates?_

1. Parse the rules and orders
2. Create a defaultdict of sets and populate the rules
3. Use this dictionary as a sort key
4. Check if the order is sorted and return required sum

One-liner compatible code:

```python
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
    if o == sorted(o, key=cmp_to_key(lambda x, y: -1 if y in d[x] else 1)):
        ret += o[len(o) // 2]

print(ret)
```

### Part B

> _What do you get if you add up the middle page numbers after correctly ordering just those updates?_

1. Step 1-3 of Part A
2. Check if the order is unsorted and return required sum from sorted order

One-liner compatible code:

```python
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
```

## Results

| Day | Time     | Rank | Score | Time     | Rank | Score |
| --- | -------- | ---- | ----- | -------- | ---- | ----- |
| 5   | 00:13:15 | 2188 | 0     | 00:40:50 | 4559 | 0     |
| 4   | 00:29:50 | 6150 | 0     | 00:42:39 | 5333 | 0     |
| 3   | 00:10:42 | 4551 | 0     | 00:32:56 | 6579 | 0     |
| 2   | 00:07:33 | 1459 | 0     | 01:00:47 | 8598 | 0     |
| 1   | 00:02:13 | 395  | 0     | 00:04:05 | 453  | 0     |
