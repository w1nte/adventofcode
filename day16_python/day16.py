import re
import sys


content = sys.stdin.read()
parsed = list(map(lambda x: x.replace('\n', ','), re.findall(r'(.*)\n\nyour ticket:\n(.*)\n\nnearby tickets:\n(.*)', content, re.DOTALL)[0]))
fields = {x[0]: (int(x[1]), int(x[2]), int(x[3]), int(x[4])) for x in re.findall(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+),?', parsed[0])}
your_tickets = list(map(lambda x: int(x), parsed[1].split(',')))
nearby_tickets = list(map(lambda x: int(x), parsed[2].split(',')))


def testvalue(f, v):
    for x in f.values():
        if (x[0] <= v <= x[1]) or (x[2] <= v <= x[3]):
            return True

    return False


print("a:", sum([x for x in nearby_tickets if not testvalue(fields, x)]))
