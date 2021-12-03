import sys
from statistics import mode

def c(l):
    a,b = (0,0)
    for x in l:
        if x == '1':
            a+=1
        if x == '0':
            b+=1
    return (a,b)

b = [sys.stdin.read().splitlines()][0]
g = [c([x[i] for x in b]) for i in range(0, len(b[0]))]

r, p = (b, 0)
while len(r) > 1:
    r = [x for x in r if x[p] == '1' and g[p][0] > g[p][1] or x[p] == '0' and g[p][0] < g[p][1] or x[p] == '1' and g[p][0] == g[p][1]]
    g = [c([x[i] for x in r]) for i in range(0, len(b[0]))]
    p += 1
    
a1 = int(''.join(r), 2)

r, p = (b, 0)
while len(r) > 1:
    r = [x for x in r if x[p] == '1' and g[p][0] < g[p][1] or x[p] == '0' and g[p][0] > g[p][1] or x[p] == '0' and g[p][0] == g[p][1]]
    g = [c([x[i] for x in r]) for i in range(0, len(b[0]))]
    p += 1

b1 = int(''.join(r), 2)

print(a1 * b1)