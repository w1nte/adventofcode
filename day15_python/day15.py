import sys

input = []
for line in sys.stdin:
    input = line.split(',')


def play(numbers, turns):
    nums = {int(i): x+1 for x, i in enumerate(input)}
    start = 0
    n = start
    for t in range(len(numbers)+1, turns):
        nsp = n
        if nsp not in nums:
            nums[nsp] = t
            n = start
            continue
        n = t - nums[n]
        nums[nsp] = t
    return n

print(play(input, 30000000))

