import sys

h, d, a = (0, 0, 0)
for c in sys.stdin.readlines():
    c, v, *_ = c.split(' ')
    v = int(v)
    match c:
        case 'forward':
            h += v
            d -= a * v
        case 'down':
            a -= v
        case 'up':
            a += v
print(h*d)