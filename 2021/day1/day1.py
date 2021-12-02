import sys, functools

c, o = -1, 0
for y in [int(x) for x in sys.stdin]:
    if y > o:
        c += 1
    o = y
print(c)