# Day 2

https://adventofcode.com/2024/day/2

## Data format

Each line contains n integers

### Part A

Constant timeout errors on the website :(

> _How many reports are safe?_

1. Create list
2. Reverse the list if it seems descending (instead of reversing we can multiply each element by -1 too)
3. Check for condition and increment counter

One-liner after parsing the input:

```python
print(sum(1 for l in lines if ((((nums := list(map(int, l.split())))[1] > nums[0]) or (nums := nums[::-1])) and all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)))))
```

TC: O(n)\
SC: O(n)

### Part B

Got too hung up on the greedy approach which turned out to be incorrect. Wasted a lot of time lol.

> _How many reports are now safe?_

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

## Mathematical Representation

Inspiration: https://x.com/0x158/status/1863514338243256670

We have a matrix defined as such:

$$
A = \begin{bmatrix}
c_{11} & c_{12} & c_{13} & \dots & c_{1j} \\
c_{21} & c_{22} & c_{23} & \dots & c_{2j} \\
c_{31} & c_{32} & c_{33} & \dots & c_{3j} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_{n1} & c_{n2} & c_{n3} & \dots & c_{nj}
\end{bmatrix}
$$

Within matrix $A$, we need to find the sum of rows where each column in the row is monotonically increasing or decreasing by either 1, 2, or 3. We can use the logical formula below to tell if a number is in the range of 1, 2, or 3:

$$
I(x) =
\begin{cases}
1 & \text{if } x \in \{1, 2, 3\} \\
0 & \text{otherwise}
\end{cases}
$$

We can use this to sum up how many columns in a given row are within this range:

$$
x = \sum_{j=1}^{m-1} I(|A_{ij} - A_{i,j+1}|)
$$

Where $A_{ij}$ is the element at row $i$ and column $j$, and $A_{i,j+1}$ is the element at row $i$ and column $j+1$.

Finally, we can use a function called **Kronecker delta**, which is defined as:

$$
\delta(a, b) =
\begin{cases}
1 & \text{if } a = b \\
0 & \text{if } a \neq b
\end{cases}
$$

### Monotonicity Check:

For a row $A_i = [A_{i1}, A_{i2}, \dots, A_{im}]$, we an express the monotonicity check as:

$$
\text{MonotonicityCheck}(A_i) =
\begin{cases}
\text{Increasing} & \text{if } A_{ij} < A_{i,j+1} \text{ for all } j \\
\text{Decreasing} & \text{if } A_{ij} > A_{i,j+1} \text{ for all } j \\
\text{Non-monotonic} & \text{otherwise}
\end{cases}
$$

### Final Sum Calculation:

Let $n$ be the number of rows in matrix $A$, and $m$ be the number of columns.

We calculate the final sum $z$ as:

$$
z = \sum_{i=1}^{n} \delta(m-1, \sum_{j=1}^{m-1} I(|A_{ij} - A_{i,j+1}|)) \cdot \mathbb{I}(\text{MonotonicityCheck}(A_i) \neq \text{Non-monotonic})
$$

### Simplified version:

For monotonically increasing: $x_i = \sum_{j=1}^{m-1} I(A_{i,j+1} - A_{ij})$ and for monotonically decreasing: $x_i = \sum_{j=1}^{m-1} I(A_{ij} - A_{i,j+1})$

And the sequence will be either monotonically increasing/decreasing:

$$
z = \sum_{i=1}^{n} \delta(m-1, \sum_{j=1}^{m-1} I(A_{i,j+1} - A_{ij})) + \sum_{i=1}^{n} \delta(m-1, \sum_{j=1}^{m-1} I(A_{ij} - A_{i,j+1}))
$$

### Python Implementation:

```python
z = 0
for l in lines:
    nums = list(map(int, l.split()))
    if all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)): z += 1
    if all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1)): z += 1
print(z)
```
