import functools

max_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0
}


def update_max_cubes(result_set):
    # Updates the max cubes for the current result set of the game.
    # An example result set is a str like: '1 blue, 8 green'
    picked_cubes = result_set.split(',')
    for picked_cube in picked_cubes:
        qty, colour = picked_cube.split()
        qty = int(qty)

        # If larger than recorded max, set it as the new max
        if qty > max_cubes[colour]:
            max_cubes[colour] = qty


with open('day2-input.txt', 'r') as f:
    lines = f.readlines()

power_values = []
for line in lines:
    # Each line represents a game
    # e.g. "Game 15: 3 green, 1 blue, 5 red; 2 red; 1 red, 4 green"
    game_label, game_text = line.split(':')
    game_id = game_label.split()[1]
    result_sets = game_text.strip().split(';')

    # Update max cube quantities for each set in the game
    for result_set in result_sets:
        update_max_cubes(result_set)

    # Multiply the max cube quantities in the current game
    power_value = functools.reduce(
        lambda x, y: x*y,
        max_cubes.values()
    )

    # Reset max cube quantities for the next game
    for colour in max_cubes:
        max_cubes[colour] = 0

    # Add power value to overall list to be summed
    power_values.append(power_value)


print(sum(power_values))  # 69929
