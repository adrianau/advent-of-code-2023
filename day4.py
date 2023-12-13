with open('day4-input.txt', 'r') as f:
    # Remove the (fixed length) card number at the start
    # e.g. 'Card   1: 55 61 75' becomes just '55 61 75'
    lines = [line[10:] for line in f.readlines()]

total_card_points = 0
for line in lines:
    # Separate the winning and owned numbers
    winning_numbers_str, owned_numbers_str = line.split('|')

    # Turn from strings into lists
    winning_numbers = winning_numbers_str.split()
    owned_numbers = owned_numbers_str.split()

    # Calculate points for current card
    card_points = 0
    for owned_num in owned_numbers:
        if owned_num in winning_numbers:
            if card_points == 0:
                card_points += 1  # First match is worth 1 point
            else:
                card_points *= 2  # Subsequent matches 2x card points

    total_card_points += card_points

print(total_card_points)  # 21919
