max_quantity = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check_valid_result_set(result_set):
    # Returns True if all cubes picked are under their max quantities
    # An example result set is a str like: '1 blue, 8 green'
    picked_cubes = result_set.split(',')
    for picked_cube in picked_cubes:
        qty, colour = picked_cube.split()
        if int(qty) > max_quantity[colour]:
            return False
    return True


with open('day2-input.txt', 'r') as f:
    lines = f.readlines()

possible_game_ids = []
for line in lines:
    game_label, game_text = line.split(':')
    game_id = game_label.split()[1]
    result_sets = game_text.strip().split(';')

    if all(check_valid_result_set(result_set) for result_set in result_sets):
        possible_game_ids.append(int(game_id))

print(sum(possible_game_ids))  # 2164
