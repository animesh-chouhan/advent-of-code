import functools

nums = list(map(int, open("input.txt").read().split()))
steps = 75


@functools.cache
def visit(num, step):
    if step == steps:
        return 1
    if num == 0:
        return visit(1, step + 1)
    s, l = str(num), len(str(num))
    if len(s) % 2 == 0:
        return visit(int(s[: l // 2]), step + 1) + visit(int(s[l // 2 :]), step + 1)
    else:
        return visit(num * 2024, step + 1)


print(sum(visit(num, 0) for num in nums))
