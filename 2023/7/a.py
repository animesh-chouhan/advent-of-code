import re
import time
import pathlib
from functools import cmp_to_key
from collections import Counter

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

# print(lines)

start_time = time.time()


def compare_card(card1, card2):
    if card1 == card2:
        return 0
    card_strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card1_index = card_strength.index(card1)
    card2_index = card_strength.index(card2)
    if card1_index > card2_index:
        return -1
    elif card1_index < card2_index:
        return 1


def compare_equal_hands(hand1, hand2):
    if hand1 == hand2:
        return 0
    for i, j in zip(hand1, hand2):
        if i == j:
            continue
        comp = compare_card(i, j)
        return comp
    return 0


def compare_hands(hand1, hand2):
    if hand1 == hand2:
        return 0
    counter1 = Counter(hand1)
    counter2 = Counter(hand2)
    # print(counter1)
    # print(counter2)
    counter1_len = len(counter1)
    counter2_len = len(counter2)
    if counter1_len > counter2_len:
        return -1
    elif counter1_len < counter2_len:
        return 1
    elif counter1_len == counter2_len:
        if counter1_len == 1:
            return compare_card(hand1[0], hand2[0])
        else:
            counter1_val = sorted(counter1.values(), reverse=True)
            counter2_val = sorted(counter2.values(), reverse=True)
            if counter1_val > counter2_val:
                return 1
            elif counter1_val < counter2_val:
                return -1
            elif counter1_val == counter2_val:
                return compare_equal_hands(hand1, hand2)


bids = {line.split()[0]: int(line.split()[1]) for line in lines}
# hands = sorted(bids.keys())
# print(compare_hands("32T3K", "KK677"))
hands = sorted(bids.keys(), key=cmp_to_key(compare_hands))

# print(hands)
winnings = []
for i, hand in enumerate(hands):
    winnings.append(bids[hand] * (i + 1))

print(sum(winnings))


print(f"Time taken: {time.time() - start_time}")
