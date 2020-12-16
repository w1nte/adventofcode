import re
import sys


# worst python code ever, don't look at it. it's not even fast. I should actually study for my exam.
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


def findorder(f, ticketgroups, i):
    if i >= len(ticketgroups[0]):
        return []
    pfields = []
    for k, v in f.items():
        allf = True
        for tickets in ticketgroups:
            if not ((v[0] <= tickets[i] <= v[1]) or (v[2] <= tickets[i] <= v[3])):
                allf = False
                break
        if allf:
            pfields.append(k)

    for p in pfields:
        nf = f.copy()
        nf.pop(p)
        next_order = findorder(nf, ticketgroups, i+1)
        solution = [p] + next_order
        if len(solution) == len(ticketgroups[0])-i:
            return solution
    return []


nearby_tickets_grouped = [nearby_tickets[x:x+len(your_tickets)] for x in range(0, len(nearby_tickets), len(your_tickets))]
nearby_valid_tickets = [t for t in nearby_tickets_grouped if all(list(map(lambda x: testvalue(fields, x), t)))]

found_order = findorder(fields, nearby_valid_tickets, 0)
print(found_order)
result = 1
for x, val in enumerate(found_order):
    if val.startswith('departure'):
        result *= your_tickets[x]
        print(x, val)
print(result)