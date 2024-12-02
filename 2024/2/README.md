# Day 2

https://adventofcode.com/2024/day/2

## Data format

Each line contains n integers

### Part A

Constant timeout errors on the website :(

> _How many reports are safe?_

1. Create list
2. Reverse the list if it seems descending
3. Check for condition and increment counter

One-liner after parsing the input:

```python
print(sum(1 for l in lines if ((((nums := list(map(int, l.split())))[1] > nums[0]) or (nums := nums[::-1])) and all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)))))
```

TC: O(n)\
SC: O(n)

### Part B

Got too hung up on the greedy approach which turned out to be incorrect. Wasted a lot of time lol.

> _What is their similarity score?_

1. Same approach as part A
2. Check for normal case
3. Check by removing each element
4. Check for condition and increment counter

One-liner after parsing the input:

```python
print(sum(1 for l in lines if (not(check := lambda nums: all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)))) or (check(nums := list(map(int, l.split())))) or (check(nums[::-1])) or any(check(nums[:i] + nums[i + 1 :]) for i in range(len(nums))) or any(check((nums[:i] + nums[i + 1 :])[::-1]) for i in range(len(nums)))))
```

TC: O(n^2)\
SC: O(n)

The time-complexity can be further reduced to O(n) by checking the full sequence only once at the first index where the condition fails. Two cases: 1. remove the current index or 2. remove the next index

TC: O(n)\
SC: O(n)

Check b1.py or b2.py!

## Results

| Day | Time     | Rank | Score | Time     | Rank | Score |
| --- | -------- | ---- | ----- | -------- | ---- | ----- |
| 2   | 00:07:33 | 1459 | 0     | 01:00:47 | 8598 | 0     |
| 1   | 00:02:13 | 395  | 0     | 00:04:05 | 453  | 0     |
