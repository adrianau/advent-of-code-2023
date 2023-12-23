import time


with open('day8-input.txt', 'r') as f:
    lines = f.readlines()

start = time.time()
directions = lines[0].strip()
directions_length = len(directions)
direction_cursor = 0

# Process lines once to add to dictionary for easy access
node_map = {}
for line in lines[2:]:
    # Create a dict of the node mappings
    # e.g. 'MQF = (DDG, LSH)' becomes { 'MQF': ('DDG', 'LSH') }
    current_node, adjacent_nodes = line.split('=')
    left_node, right_node = adjacent_nodes.split(',')
    left_node = left_node.replace('(', '').strip()
    right_node = right_node.replace(')', '').strip()
    node_map[current_node.strip()] = (left_node, right_node)

step_count = 0
current_node = 'AAA'  # Start node
while True:
    if current_node == 'ZZZ':
        break

    # Current direction points to next node tuple
    # node[0] is left path, node[1] is right path
    current_direction = directions[direction_cursor]
    if current_direction == 'L':
        current_node = node_map[current_node][0]
    else:
        current_node = node_map[current_node][1]

    # Update cursor to next position (cyclic)
    direction_cursor += 1
    if direction_cursor == directions_length:
        direction_cursor = 0

    step_count += 1  # Increment step count

end = time.time()
print(f'Reached ZZZ after {step_count} steps')  # 12083
print(f'Took {end - start} seconds')  # 4ms
