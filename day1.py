calibration_values = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    calibration_value = ""

    for char in line:
        if char.isdigit():
            calibration_value += char

    calibration_value = calibration_value[0] + calibration_value[-1]
    calibration_values.append(int(calibration_value))

print(sum(calibration_values))  # 56042