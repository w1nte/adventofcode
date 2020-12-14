import sys
import re


def apply_mask(mask, value):
    result = list("{0:b}".format(int(value)).zfill(len(mask)-1))
    for i in range(len(mask)):
        if mask[i] == '1':
            result[i] = '1'
        elif mask[i] == '0':
            result[i] = '0'
    return "".join(result)


mem = {}
mask = ""

for line in sys.stdin:
    if line[0:4] == 'mask':
        mask = line[7:]
    else:
        pos, value = re.findall(r'mem\[(\d+)\] = (\d+)', line)[0]
        mem[pos] = int(apply_mask(mask, value), 2)


print(sum(mem.values()))

