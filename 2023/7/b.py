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
    card_strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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


def modify_counter_val_for_j(counter):
    j_count = counter.get("J", 0)
    if j_count == 0 or j_count == 5:
        return sorted(counter.values(), reverse=True)
    else:
        del counter["J"]
        counter_val = sorted(counter.values(), reverse=True)
        counter_val[0] += j_count
        return counter_val


def compare_hands(hand1, hand2):
    if hand1 == hand2:
        return 0
    counter1 = Counter(hand1)
    counter2 = Counter(hand2)
    # print(counter1)
    # print(counter2)

    counter1_val = modify_counter_val_for_j(counter1)
    counter2_val = modify_counter_val_for_j(counter2)

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
