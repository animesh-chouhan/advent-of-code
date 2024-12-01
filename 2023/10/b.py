import re
import time
import pathlib
from functools import cmp_to_key
from collections import Counter
import sys

# import numpy as np
# from PIL import Image

sys.setrecursionlimit(50000)

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()

directions = {"right": 0 + 1j, "left": 0 - 1j, "up": -1 + 0j, "down": 1 + 0j}

grid = [list(line) for line in lines]
# print(grid)
grid_x = len(grid)
grid_y = len(grid[0])

path = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
symbols = []

area = 0


def move(start, step, steps, dir):
    global area, symbols
    # print(start, step)
    end_complex = start + step
    if end_complex.real < 0 or end_complex.real >= grid_x:
        return -1
    if end_complex.imag < 0 or end_complex.imag >= grid_y:
        return -1

    symbol = grid[int(end_complex.real)][int(end_complex.imag)]
    symbols.append(symbol)
    path[int(end_complex.real)][int(end_complex.imag)] = 1
    # print(symbol)
    area_current = grid_x - 1 - int(end_complex.real)
    print(area)

    if symbol == "S":
        return steps + 1
    elif symbol == ".":
        return -1
    elif symbol == "|":
        if step == (-1 + 0j):
            return move(end_complex, (-1 + 0j), steps + 1, dir)
        elif step == (1 + 0j):
            return move(end_complex, (1 + 0j), steps + 1, dir)
        else:
            return -1
    elif symbol == "-":
        if step == (0 + 1j):
            area += area_current
            return move(end_complex, (0 + 1j), steps + 1, dir)
        elif step == (0 - 1j):
            area -= area_current
            return move(end_complex, (0 - 1j), steps + 1, dir)
        else:
            return -1
    elif symbol == "L":
        if step == (1 + 0j):
            area += area_current
            return move(end_complex, (0 + 1j), steps + 1, dir)
        elif step == (0 - 1j):
            area -= area_current
            return move(end_complex, (-1 + 0j), steps + 1, dir)
        else:
            return -1
    elif symbol == "J":
        if step == (1 + 0j):
            area -= area_current
            return move(end_complex, (0 - 1j), steps + 1, dir)
        elif step == (0 + 1j):
            area += area_current
            return move(end_complex, (-1 + 0j), steps + 1, dir)
        else:
            return -1
    elif symbol == "7":
        if step == (-1 + 0j):
            area -= area_current
            return move(end_complex, (0 - 1j), steps + 1, dir)
        elif step == (0 + 1j):
            area += area_current
            return move(end_complex, (1 + 0j), steps + 1, dir)
        else:
            return -1
    elif symbol == "F":
        if step == (-1 + 0j):
            area += area_current
            return move(end_complex, (0 + 1j), steps + 1, dir)
        elif step == (0 - 1j):
            area -= area_current
            return move(end_complex, (1 + 0j), steps + 1, dir)
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

for to in list(directions.values())[1:]:
    print(start_point)
    out = move(start_point, to, 0, 1)
    # print(out)
    if out != -1:
        print("found")
        print(out)
        break
    else:
        area = 0
        symbols = []
        path = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

# for line in path:
#     print(line)
# print(grid_x * grid_y)
print(area)
print(symbols)
print(f"Time taken: {time.time() - start_time}")
