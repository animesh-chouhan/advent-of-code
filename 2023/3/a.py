import re
import time
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

start_time = time.time()

symbols = "~`!@#$%^&*()_+-=/"

engine_parts = []
for i, line in enumerate(lines):
    nums = re.finditer("\d+", line)
    for num in nums:
        # print(num)
        # print(num.group(0))
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
                fsymbols.append(lines[i - 1][j])
                flags.append(lines[i - 1][j] in symbols)
            except IndexError:
                fsymbols.append(-1)
                flags.append(False)

        try:
            if start - 1 < 0:
                raise IndexError
            fsymbols.append(lines[i][start - 1])
            flags.append(lines[i][start - 1] in symbols)
        except IndexError:
            fsymbols.append(-1)
            flags.append(False)

        try:
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

        if any(flags):
            engine_parts.append(int(num.group(0)))


# print(engine_parts)
print(sum(engine_parts))
print(f"Time taken: {time.time() - start_time}")
