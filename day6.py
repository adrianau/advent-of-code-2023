def get_distance(hold_time, race_time):
    # Calculate distance travelled based on hold time and race time
    movement_time = race_time - hold_time
    speed = hold_time  # Redundant, but kept for clarity
    distance_travelled = speed * movement_time
    print(f'Hold {hold_time}ms, travelled {distance_travelled}mm at {speed}mm/ms over {movement_time}ms')

    return distance_travelled


if __name__ == '__main__':
    with open('day6-input.txt', 'r') as f:
        lines = f.readlines()

    # Combine race times and record distances into single number
    # e.g. 'Time: 7 15 30' -> 71530; 'Distance: 9 40 200' -> 940200
    race_time = int(''.join(lines[0].split()[1:]))
    record_distance = int(''.join(lines[1].split()[1:]))

    record_beating_count = 0

    # Check distance travelled for all possible hold times
    # If it beats the distance record, increment the count
    for hold_time in range(1, race_time):
        distance = get_distance(hold_time, race_time)
        if distance > record_distance:
            record_beating_count += 1

    # TODO: Optimise solution
    print(record_beating_count)  # 35150181
