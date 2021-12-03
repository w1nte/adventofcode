import sys, re

l = [int(x) for x in sys.stdin]
nl = [l[i] + l[i-1] + l[i+1] for i in range(1, len(l)-1)]
c, o = -1, 0
for y in nl:
    if y > o:
        c += 1
    o = y
print(c)
