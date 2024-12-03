# Day 1

https://adventofcode.com/2024/day/3

Just use regex lol.

## Data format

The whole input contains some mul operations and other corrupted data. Faced an issue with the newline char by treating it as a seperate testcase and resetting the flag.

### Part A

> _What do you get if you add up all of the results of the multiplications?_

1. Create a regex with capture group to get mul(x,y)
2. Find matches and sum the mul operation

One-liner after parsing the input:

```python
print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", open('input.txt').read())))
```

### Part B

> _what do you get if you add up all of the results of just the enabled multiplications?_

1. Create a regex which matches mul(x,y) or do() or don't()
2. Find matches and update the flag when do()/don't() is encountered
3. Sum the enabled mul operations

One-liner after parsing the input: A bit complicated due to flag.

```python
print(sum(int(x) * int(y) for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()) if (flag := (match == "do()") or (match != "don't()" and globals().get("flag", True))) and match.startswith("mul(") for x, y in [match[4:-1].split(",")]))
```

## Results

| Day | Time     | Rank | Score | Time     | Rank | Score |
| --- | -------- | ---- | ----- | -------- | ---- | ----- |
| 3   | 00:10:42 | 4551 | 0     | 00:32:56 | 6579 | 0     |
| 2   | 00:07:33 | 1459 | 0     | 01:00:47 | 8598 | 0     |
| 1   | 00:02:13 | 395  | 0     | 00:04:05 | 453  | 0     |
