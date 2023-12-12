from string import punctuation
from itertools import product

# String of symbols without the period
symbols = punctuation.replace('.', '')


def char_at(x, y):
    # Grid is accessed by (y,x) which can be confusing.
    # This func inverts it so access can be done by (x,y).
    try:
        return grid[y][x]
    except IndexError:
        print(f"Trying to access row {y} (y) col {x} (x)")


def get_part_number_range(x, y):
    # Scans to start/end positions of a digit to get the full number.
    # Digits comprise a number until it hits grid boundaries or a symbol.
    start_x = end_x = x
    while True:
        if start_x == 0 or char_at(start_x-1, y) in punctuation:
            break
        start_x -= 1

    # Number range will be sliced, so end_x index is exclusive (+1)
    while True:
        end_x += 1
        if end_x == grid_length or char_at(end_x, y) in punctuation:
            break

    return start_x, end_x, y


def get_adjacent_digit_positions(x, y):
    # Determine valid adjacent positions
    valid_x = [x]
    valid_y = [y]
    if x > 0:
        valid_x.append(x-1)
    if x < len(grid[0]) - 1:
        valid_x.append(x+1)
    if y > 0:
        valid_y.append(y-1)
    if y < len(grid) - 1:
        valid_y.append(y+1)

    # Get all permutations of valid positions
    valid_adjacent_positions = list(product(valid_x, valid_y))

    # 1. Filter to only get positions with digits
    # 2. Sort position by row number (y) then by col number (x)
    #    (This will be helpful later when extracting the
    #     first and last digits of a part number in a row)
    return sorted(
        filter(
            lambda pos: char_at(pos[0], pos[1]).isdigit(),
            valid_adjacent_positions
        ),
        key=lambda coord: (coord[1], coord[0])
    )


with open('day3-input.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]
    grid_length = len(grid)  # Assuming equal grid

part_numbers = []
for row_num, row in enumerate(grid):
    for col_num, char in enumerate(row):
        if char in symbols:
            # If this char is a symbol, check for adjacent digits
            adjacent_positions = get_adjacent_digit_positions(col_num, row_num)

            # Ignore if no adjacent digits at position
            if not adjacent_positions:
                continue

            # Find start/end positions of adjacent digits to get full number
            end_x = target_y = -1
            for x, y in adjacent_positions:
                # Ignore digit if part of number that was already processed
                if y == target_y and x <= end_x:
                    continue

                # Use positions above to extract the part number
                start_x, end_x, target_y = get_part_number_range(x, y)
                part_number = grid[y][start_x:end_x]
                part_numbers.append(int(part_number))

print(sum(part_numbers))  # 531561
