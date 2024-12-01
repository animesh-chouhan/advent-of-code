# Day 2

https://adventofcode.com/2024/day/2

## Data format

Each line contains 2 numbers which are part of lists l1, l2 respectively.

### Part A

> _What is the total distance between your lists?_

1. Create lists
2. Sort both lists
3. Find abs(e1-e2) and return sum

One-liner after parsing the input:

```python
print(sum(abs(a - b) for a, b in zip(*[sorted(x) for x in zip(*[map(int, line.split()) for line in lines])])))
```

TC: O(nlogn)
SC: O(n)

### Part B

> _What is their similarity score?_

1. Create lists
2. Create a counter of list2
3. Iterate over list1, calculate the score and return sum

Instead of calling count for each element in list1, we can build a counter which reduces our TC from O(n^2) to O(n).

One-liner after parsing the input:

```python
print(sum(e * Counter(map(int, (l.split()[1] for l in lines)))[e] for e in map(int, (l.split()[0] for l in lines))))
```

TC: O(n)
SC: O(n)

## Results

| Day | Part | Time     | Rank | Score |
| --- | ---- | -------- | ---- | ----- |
| 1   | 1    | 00:02:13 | 395  | 0     |
| 1   | 2    | 00:04:05 | 453  | 0     |
