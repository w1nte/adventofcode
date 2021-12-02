import sys
import re


def apply_mask(mask, value):
    result = list("{0:b}".format(int(value)).zfill(len(mask)-1))
    for i in range(len(mask)):
        if mask[i] == '1':
            result[i] = '1'
        elif mask[i] == 'X':
            result[i] = 'X'
    return "".join(result)


def generate_addrs(floatingaddr):
    l = list(floatingaddr)
    for i in range(len(l)):
        if l[i] == 'X':
            t1 = generate_addrs(['0'] + l[i + 1:])
            t2 = generate_addrs(['1'] + l[i + 1:])

            return list(map(lambda t: l[:i] + t, t1 + t2))
    return [l]


mem = {}
mask = ""

for line in sys.stdin:
    if line[0:4] == 'mask':
        mask = line[7:]
    else:
        pos, value = re.findall(r'mem\[(\d+)\] = (\d+)', line)[0]
        addrs = list(map(lambda a : "".join(a), generate_addrs(apply_mask(mask, pos))))
        for addr in addrs:
            mem[int(addr, 2)] = int(value)

print(sum(mem.values()))

