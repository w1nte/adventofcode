import sys

l = [[int(c) for c in x if c.isnumeric()] for x in sys.stdin]
n = [x[0] * 10 + x[-1] for x in l]
print(sum(n))