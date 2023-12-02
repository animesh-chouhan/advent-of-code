import pathlib


def main(lines):
    print(lines)
    for line in lines:
        pass


parent_path = pathlib.Path(__file__).parent.resolve()
test_input_path = parent_path / "test.txt"
main_input_path = parent_path / "input.txt"

with open(test_input_path) as f:
    lines = f.read().split("\n")
main(lines)
input()
with open(main_input_path) as f:
    lines = f.read().split("\n")
main(lines)
