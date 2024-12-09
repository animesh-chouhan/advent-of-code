import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().strip()


nums = list(map(int, lines))
disk = []
for l in range(len(nums)):
    if l % 2 == 0:
        disk.extend([l // 2] * nums[l])
    else:
        disk.extend([-1] * nums[l])


l = 0
r = len(disk) - 1
while r > 0:

    while disk[r] == -1:
        r -= 1

    startj = r
    while disk[startj] == disk[r]:
        startj -= 1
    blockj = r - startj

    l = 0
    while l < r:
        while l < r and disk[l] != -1:
            l += 1

        endi = l
        while endi < len(disk) and disk[endi] == -1:
            endi += 1
        blocki = endi - l

        if l > r:
            break

        # print(disk[r], blockj, blocki, endi, l)
        if blocki >= blockj:
            for _ in range(blockj):
                disk[l], disk[r] = disk[r], disk[l]
                l += 1
                r -= 1
            break
        else:
            l = endi

    r = startj

print(sum(l * e for l, e in enumerate(disk) if e != -1))
