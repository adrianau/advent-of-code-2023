from functools import reduce


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

    # Extract int list of race times and record distances from input
    race_times = [int(time) for time in lines[0].split()[1:]]
    record_distances = [int(distance) for distance in lines[1].split()[1:]]

    # Get a list of 2-tuples of race time and matching record distance
    # e.g. (7, 9) = 7ms race time with a record distance of 9mm
    race_records = zip(race_times, record_distances)

    record_beating_counts = []
    for race_time, peak_distance in race_records:
        record_beating_count = 0

        # Check distance travelled for all possible hold times
        # If it beats the distance record, increment the count
        for hold_time in range(1, race_time):
            distance = get_distance(hold_time, race_time)
            if distance > peak_distance:
                record_beating_count += 1

        record_beating_counts.append(record_beating_count)

    # Multiply the num of record beating ways for each race
    record_beating_product = reduce(
        lambda acc, x: acc * x,
        record_beating_counts
    )

    print(record_beating_product)  # 293046
