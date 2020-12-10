import sys

input = list(map(lambda x: int(x), sys.stdin))
input.append(0)
input = sorted(input)
charging_outlet = 0
device_joltage = input[-1] + 3
input.append(device_joltage)

diff_map = {1: 0, 2: 0, 3: 0}
groups = []
group_count = 0
current_joltage = charging_outlet
for joltage in input:
    difference = joltage - current_joltage
    if 0 < difference <= 3:
        diff_map[difference] += 1
        current_joltage = joltage

    if difference == 3:
        groups.append(group_count)
        group_count = 0

    group_count += 1

groups.append(group_count)

t = 1
for g in groups:
    if g == 3:
        t *= 2
    if g == 4:
        t *= 4
    if g == 5:
        t *= 7

print(diff_map[1] * diff_map[3])
print(t)