import re
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

symbols = "*"

gears = {}
for i, line in enumerate(lines):
    nums = re.finditer("\d+", line)
    for num in nums:
        print(num)
        print(num.group(0))
        num_int = int(num.group(0))
        start = num.start()
        end = num.end() - 1
        num_len = end - start + 1
        # print(start, end)
        flags = []
        fsymbols = []
        for j in range(start - 1, end + 2):
            try:
                if i - 1 < 0 or j < 0:
                    raise IndexError
                if lines[i - 1][j] in symbols:
                    if (i - 1, j) not in gears.keys():
                        gears[(i - 1, j)] = [num_int]
                    else:
                        gears[(i - 1, j)].append(num_int)
                fsymbols.append(lines[i - 1][j])
                flags.append(lines[i - 1][j] in symbols)
            except IndexError:
                fsymbols.append(-1)
                flags.append(False)

        try:
            if start - 1 < 0:
                raise IndexError
            if lines[i][start - 1] in symbols:
                if (i, start - 1) not in gears.keys():
                    gears[(i, start - 1)] = [num_int]
                else:
                    gears[(i, start - 1)].append(num_int)
            fsymbols.append(lines[i][start - 1])
            flags.append(lines[i][start - 1] in symbols)
        except IndexError:
            fsymbols.append(-1)
            flags.append(False)

        try:
            if lines[i][end + 1] in symbols:
                if (i, end + 1) not in gears.keys():
                    gears[(i, end + 1)] = [num_int]
                else:
                    gears[(i, end + 1)].append(num_int)
            fsymbols.append(lines[i][end + 1])
            flags.append(lines[i][end + 1] in symbols)
        except IndexError:
            fsymbols.append(-1)
            flags.append(False)

        for j in range(start - 1, end + 2):
            # print(i, j)
            try:
                if i < 0 or j < 0:
                    raise IndexError
                if lines[i + 1][j] in symbols:
                    if (i + 1, j) not in gears.keys():
                        gears[(i + 1, j)] = [num_int]
                    else:
                        gears[(i + 1, j)].append(num_int)
                fsymbols.append(lines[i + 1][j])
                flags.append(lines[i + 1][j] in symbols)
            except IndexError:
                fsymbols.append(-1)
                flags.append(False)

        assert len(fsymbols) == 2 * (num_len + 2) + 2
        assert len(flags) == 2 * (num_len + 2) + 2

        # print(fsymbols)
        # print(flags)
        # print(list(zip(fsymbols, flags)))
        # print(any(flags))
        # input()

print(gears)
gear_ratios = []
for k, v in gears.items():
    if len(v) == 2:
        gear_ratios.append(v[0] * v[1])

print(sum(gear_ratios))
