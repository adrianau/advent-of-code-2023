card_copies = {}


def increment_copies(card_num, amount):
    # Increment the number of copies of a card by an amount
    # Initialises it to the amount if not in dict
    if card_num in card_copies:
        card_copies[card_num] += amount
    else:
        card_copies[card_num] = amount


with open('day4-input.txt', 'r') as f:
    # Remove the (fixed length) card number at the start
    # e.g. 'Card   1: 55 61 75' becomes just '55 61 75'
    lines = [line[10:] for line in f.readlines()]

for card_num, line in enumerate(lines, 1):
    # Increment count for current card
    increment_copies(card_num, 1)

    # Separate the winning and owned numbers
    winning_numbers_str, owned_numbers_str = line.split('|')

    # Turn from strings into lists
    winning_numbers = winning_numbers_str.split()
    owned_numbers = owned_numbers_str.split()

    # Count n winning matches for the card
    winning_matches = 0
    for owned_num in owned_numbers:
        if owned_num in winning_numbers:
            winning_matches += 1

    # Increment copies of next n cards by the number of copies of this card
    for i in range(1, winning_matches + 1):
        target_card_num = card_num + i
        increment_copies(target_card_num, card_copies[card_num])

print(sum(card_copies.values()))  # 9881048
