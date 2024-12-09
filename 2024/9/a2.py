data = list(map(int, open("input.txt").read().strip()))
disk = []
for i in range(len(data)):
    if i % 2 == 0:
        disk.extend([i // 2] * data[i])
    else:
        disk.extend([-1] * data[i])

l = 0
r = len(disk) - 1
while True:
    while disk[l] != -1:
        l += 1
    while disk[r] == -1:
        r -= 1
    if l < r:
        disk[l], disk[r] = disk[r], disk[l]
    else:
        break

print(sum(i * e for i, e in enumerate(disk) if e != -1))
