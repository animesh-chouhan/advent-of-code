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

        # print(symbols_found)
        # print(flags)
        # print(list(zip(symbols_found, flags)))
        # print(any(flags))
        # input()
        # assert len(symbols_found) == 2 * (num_len + 2) + 2
        # assert len(flags) == 2 * (num_len + 2) + 2

        if any(flags):
            engine_parts.append(num_int)


# print(engine_parts)
print(sum(engine_parts))
print(f"Time taken: {time.time() - start_time}")
