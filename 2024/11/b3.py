import functools
from math import log
import sys

sys.setrecursionlimit(15000)
nums = list(map(int, open("input.txt").read().split()))
steps = 2000


@functools.cache
def visit(num, step):
    if step == steps:
        return 1
    if num == 0:
        return visit(1, step + 1)
    l = int(log(num, 10)) + 1
    d = pow(10, l // 2)
    if l % 2 == 0:
        return visit(num // d, step + 1) + visit(num % d, step + 1)
    else:
        return visit(num * 2024, step + 1)


print(sum(visit(num, 0) for num in nums))
