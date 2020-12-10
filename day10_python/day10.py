import sys

input = sorted(list(map(lambda x: int(x), sys.stdin)))
charging_outlet = 0
device_joltage = input[-1] + 3
input.append(device_joltage)

diff_map = {1: 0, 2: 0, 3: 0}
current_joltage = charging_outlet
for joltage in input:
    difference = joltage - current_joltage
    if 0 < difference <= 3:
        diff_map[difference] += 1
        current_joltage = joltage

print(diff_map[1] * diff_map[3])