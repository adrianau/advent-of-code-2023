from string import punctuation
from itertools import product

# String of symbols without the period
symbols = punctuation.replace('.', '')


def pos(x, y):
    # Grid is accessed by (y,x) which can be confusing
    # So accessing via this func inverts it for you
    try:
        return grid[y][x]
    except Exception:
        print(f"Trying to access row {y} (y) char {x} (x)")


def check_start_digit(x, y):
    if x == 0:
        return False
    return pos(x-1, y) in symbols + '.'


def check_end_digit(x, y):
    if x == grid_length:
        return False

    return pos(x+1, y) in symbols + '.'


def get_start_digit_x(x, y):
    current_x = x
    while True:
        if current_x == 0:
            return current_x

        if check_start_digit(current_x, y):
            return current_x

        current_x -= 1


def get_end_digit_x(x, y):
    current_x = x
    while True:
        if current_x == (grid_length - 1):
            return current_x

        if check_end_digit(current_x, y):
            return current_x

        current_x += 1


def get_digits(adjacent_coords):
    # Checks if adjacent coordinates have digits and returns them
    adjacent_digit_coords = []
    for x, y in adjacent_coords:
        if pos(x, y).isdigit():
            adjacent_digit_coords.append((x, y))

    return adjacent_digit_coords


def check_adjacent(grid, x, y):
    # Check if there are digits in the adjacent tiles
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

    # Get all the possible combinations of the valid co-ordinates
    adjacent_coords = list(product(valid_x, valid_y))

    # Sort it by row number, then by col number
    # (This will be helpful later on when determining
    # the first and last digits of number in a row)
    adjacent_coords.sort(key=lambda x: (x[1], x[0]))
    print(f'({x},{y}):', adjacent_coords)

    return adjacent_coords


with open('day3-input.txt', 'r') as f:
    lines = f.readlines()

grid = [line.strip() for line in lines]

# Grid dimensions (row length x column length)
print(f'The grid is {len(grid[0])}x{len(grid)}')
grid_length = len(grid)  # Assuming equal grid

part_numbers = []
for row_num, row in enumerate(grid):
    for col_num, char in enumerate(row):
        if char in symbols:
            adjacent_coords = check_adjacent(grid, col_num, row_num)
            adjacent_digit_coords = get_digits(adjacent_coords)

            # Keep going if no adjacent digits to work with
            if not adjacent_digit_coords:
                continue

            start_digit_x = -1
            end_digit_x = -1
            target_row = -1
            for x, y in adjacent_digit_coords:
                print(f'({x}, {y}) contains a number: {pos(x, y)}')

                # Ignore if within number range that we've evaluated before
                if y == target_row and x >= start_digit_x and x <= end_digit_x:
                    continue

                start_digit_x = get_start_digit_x(x, y)
                end_digit_x = get_end_digit_x(x, y)
                target_row = y
                print(f'Set start: {start_digit_x} | end: {end_digit_x}')

                full_part_number = grid[y][start_digit_x:end_digit_x+1]
                print('Part number:', full_part_number)
                part_numbers.append(int(full_part_number))

print(sum(part_numbers))  # 531561
