calibration_values = []

num_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

for line in lines:
    calibration_value = ''
    window = ''  # A moving window to check for number words

    for char in line:
        window += char

        # Add value if numerical digit and reset window
        if char.isdigit():
            calibration_value += char
            window = ''
            continue

        # Else, check if window contains a number word
        for num_word in num_map.keys():
            if num_word in window:
                calibration_value += num_map[num_word]
                # Reset window to last letter for cases like `eighthree`
                window = window[-1]

    calibration_value = calibration_value[0] + calibration_value[-1]
    calibration_values.append(int(calibration_value))

print(sum(calibration_values))  # 55358
