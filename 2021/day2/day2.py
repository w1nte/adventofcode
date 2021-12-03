import sys

h, d = (0, 0)
for c in sys.stdin.readlines():
    c, v, *_ = c.split(' ')
    v = int(v)
    match c:
        case 'forward':
            h += v
        case 'down':
            d += v
        case 'up':
            d -= v
print(h*d)