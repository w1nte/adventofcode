import sys
from statistics import mode

b = [sys.stdin.read().splitlines()][0]
g = int(''.join([mode([x[i] for x in b]) for i in range(0, len(b[0]))]), 2)
e = int(''.join(['0' if mode([x[i] for x in b]) == '1' else '1' for i in range(0, len(b[0]))]), 2)

print(g*e)