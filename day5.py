def recursive_convert(resource, map_idx, map_ranges, lines):
    # Converts a resource when given a map (`map_idx`)
    # This recursively converts the input resource through to the last mapping

    # Get the map range of the current map
    map_start, map_end = map_ranges[map_idx]

    for line in lines[map_start:map_end]:
        destination, source, window = [int(num) for num in line.split()]

        # If within map range, set the corresponding destination
        if resource >= source and resource <= source + (window - 1):
            delta = resource - source
            converted_resource = destination + delta
            break
    else:
        # If not within map range, set to input resource value
        converted_resource = resource

    # Return output value if we're on the last map
    if map_idx == len(map_ranges) - 1:
        return converted_resource

    # Otherwise, convert the new output in the next map
    return recursive_convert(
        converted_resource, map_idx + 1, map_ranges, lines
    )


def get_map_ranges(lines):
    # Compute a list of map ranges
    # A map range is a 2-element list of the start/end indices of a map
    # e.g. [3,10] = map starts at index 3 (incl.), ends at index 10 (excl.)
    map_ranges = []
    input_length = len(lines)
    for idx, line in enumerate(lines):
        # If end of input (which is not a new line), set end index to -1
        if idx == input_length - 1:
            map_ranges[-1].append(-1)
            break

        # If blank line, end current map range and start the next one
        if line == '\n':
            if map_ranges:
                map_ranges[-1].append(idx)  # Add end index to current map

            map_ranges.append([idx+2])  # Add start index of the next map

    return map_ranges


if __name__ == '__main__':
    with open('day5-input.txt', 'r') as f:
        lines = f.readlines()

    # Get list of seed numbers from its string
    # e.g. 'seeds: 79 14 55' -> [79, 14, 55]
    initial_seeds = [
        int(seed)
        for seed in lines[0].split(':')[1].strip().split()
    ]

    # Get the index ranges for each map
    map_ranges = get_map_ranges(lines)

    # Run through maps to get location of the initial seeds
    locations = [
        recursive_convert(seed, 0, map_ranges, lines)
        for seed in initial_seeds
    ]

    # Get the lowest location number
    print(min(locations))  # 650599855
