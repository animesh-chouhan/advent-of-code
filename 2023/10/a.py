import re
import time
import pathlib
from functools import cmp_to_key
from collections import Counter
import sys

sys.setrecursionlimit(50000)

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()

directions = {"up": 0 + 1j, "down": 0 - 1j, "left": -1 + 0j, "right": 1 + 0j}

grid = [list(line) for line in lines]
# print(grid)


def move(start, step, steps=0):
    end_complex = start + step
    if end_complex.real < 0 or end_complex.real >= len(grid[0]):
        return -1
    if end_complex.imag < 0 or end_complex.imag >= len(grid):
        return -1

    symbol = grid[int(end_complex.real)][int(end_complex.imag)]
    # print(symbol)
    if symbol == "S":
        return steps + 1
    elif symbol == ".":
        return -1
    elif symbol == "|":
        if step == (-1 + 0j):
            return move(end_complex, (-1 + 0j), steps + 1)
        elif step == (1 + 0j):
            return move(end_complex, (1 + 0j), steps + 1)
        else:
            return -1
    elif symbol == "-":
        if step == (0 + 1j):
            return move(end_complex, (0 + 1j), steps + 1)
        elif step == (0 - 1j):
            return move(end_complex, (0 - 1j), steps + 1)
        else:
            return -1
    elif symbol == "L":
        if step == (1 + 0j):
            return move(end_complex, (0 + 1j), steps + 1)
        elif step == (0 - 1j):
            return move(end_complex, (-1 + 0j), steps + 1)
        else:
            return -1
    elif symbol == "J":
        if step == (1 + 0j):
            return move(end_complex, (0 - 1j), steps + 1)
        elif step == (0 + 1j):
            return move(end_complex, (-1 + 0j), steps + 1)
        else:
            return -1
    elif symbol == "7":
        if step == (-1 + 0j):
            return move(end_complex, (0 - 1j), steps + 1)
        elif step == (0 + 1j):
            return move(end_complex, (1 + 0j), steps + 1)
        else:
            return -1
    elif symbol == "F":
        if step == (-1 + 0j):
            return move(end_complex, (0 + 1j), steps + 1)
        elif step == (0 - 1j):
            return move(end_complex, (1 + 0j), steps + 1)
        else:
            return -1


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_point = complex(i, j)
            break
    else:
        continue
    break

for to in directions.values():
    print(start_point)
    out = move(start_point, to)

    if out != -1:
        print("found")
        print(out // 2)
        break

print(f"Time taken: {time.time() - start_time}")
