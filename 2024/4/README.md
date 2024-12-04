# Day 4

https://adventofcode.com/2024/day/4

## Data format

Each line contains 2 numbers which are part of lists l1, l2 respectively.

### Part A

> _How many times does XMAS appear?_

1. Look for X
2. Create a 8 direction list
3. Match the string by iterating in that direction

One-liner after parsing the input:

```python
print(sum(1 for i in range(len(lines)) for j in range(len(lines[0])) for mi, mj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)] if all(0 <= i + mi * k < len(lines) and 0 <= j + mj * k < len(lines[0]) and lines[i + mi * k][j + mj * k] == "XMAS"[k] for k in range(len("XMAS")))))
```

TC: O(n^2 \* k)\
SC: O(1)

### Part B

> _How many times does an X-MAS appear?_

1. Look for X
2. Match the possible patterns in all directions

One-liner after parsing the input:

```python
print(sum(1 for i in range(1, len(lines) - 1) for j in range(1, len(lines[0]) - 1) if lines[i][j] == "A" and "".join([lines[i + x][j + y] for x, y in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]) in ["MSSM", "MMSS", "SSMM", "SMMS"]))
```

TC: O(n^2 \* k)\
SC: O(1)

## Results

| Day | Time     | Rank | Score | Time     | Rank | Score |
| --- | -------- | ---- | ----- | -------- | ---- | ----- |
| 4   | 00:29:50 | 6150 | 0     | 00:42:39 | 5333 | 0     |
| 3   | 00:10:42 | 4551 | 0     | 00:32:56 | 6579 | 0     |
| 2   | 00:07:33 | 1459 | 0     | 01:00:47 | 8598 | 0     |
| 1   | 00:02:13 | 395  | 0     | 00:04:05 | 453  | 0     |
