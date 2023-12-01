import sys

d = {
    'oneight': 18,
    'twone': 21,
    'fiveight': 58,
    'sevenine': 79,
    'eightwo': 82,
    'eighthree': 83,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
def r(x: str):
    for a, b in d.items():
        x = x.replace(a, str(b))
    return x

l = [[int(c) for c in r(x) if c.isnumeric()] for x in sys.stdin]
n = [x[0] * 10 + x[-1] for x in l]
print(sum(n))