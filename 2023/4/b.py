import re
import time
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

start_time = time.time()

card_count = {i: 1 for i in range(1, len(lines) + 1)}
# print(card_count)

for i, line in enumerate(lines):
    card_num = int(line.split(":")[0].split()[1])
    # print(card_num)
    numbers = line.split(":")[1]
    win_num = numbers.split("|")[0].split()
    our_num = numbers.split("|")[1].split()
    # print(win_num)
    # print(our_num)

    temp = [num for num in our_num if num in win_num]
    # print(len(temp))
    if temp:
        cards_won = [
            i for i in range(card_num + 1, card_num + len(temp) + 1) if i <= len(lines)
        ]
        # print(cards_won)
        for _ in range(card_count[card_num]):
            for card in cards_won:
                card_count[card] = card_count[card] + 1

        # print(card_count)


print(sum(card_count.values()))
print(f"Time taken: {time.time() - start_time}")
