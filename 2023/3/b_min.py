import re
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

symbols = "*"

gears = {}
for l, line in enumerate(lines):
    nums = re.finditer("\d+", line)
    for num in nums:
        # print(num)
        # print(num.group(0))
        num_int = int(num.group(0))
        start = num.start()
        end = num.end()
        num_len = end - start
        # print(start, end)
        flags = []
        symbols_found = []

        for i in range(l - 1, l + 2):
            for j in range(start - 1, end + 1):
                # print(i, j)
                if (i < 0) or (i > len(lines) - 1) or (j < 0) or (j > len(line) - 1):
                    symbols_found.append(-1)
                    flags.append(False)
                    continue
                if (i == l) and (num.start() <= j < num.end()):
                    # print(i, j)
                    continue

                symbols_found.append(lines[i][j])
                flags.append(lines[i][j] in symbols)

                if lines[i][j] in symbols:
                    if (i, j) not in gears.keys():
                        gears[(i, j)] = [num_int]
                    else:
                        gears[(i, j)].append(num_int)

        # print(symbols_found)
        # print(flags)
        # print(list(zip(symbols_found, flags)))
        # print(any(flags))
        # input()
        # assert len(symbols_found) == 2 * (num_len + 2) + 2
        # assert len(flags) == 2 * (num_len + 2) + 2

print(gears)
gear_ratios = []
for k, v in gears.items():
    if len(v) == 2:
        gear_ratios.append(v[0] * v[1])

print(sum(gear_ratios))
