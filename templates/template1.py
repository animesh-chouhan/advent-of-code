import time
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

start_time = time.time()

for line in lines:
    pass


print(f"Time taken: {time.time() - start_time}")
