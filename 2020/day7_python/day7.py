import sys
import re

bagmap = {}
for line in sys.stdin:
    parsed = list(map(lambda x: [x[0], list(map(lambda y: re.findall(r'(\d+) (.*) bags?', y.strip()), x[1].split(',')))], re.findall(r'(.*) bags contain (.*)\.', line)))[0]
    bagmap[parsed[0]] = list(map(lambda x: (x[0][1], x[0][0]), filter(lambda x: len(x) > 0, parsed[1])))

def shiny_gold(bag):
    if bag not in bagmap.keys():
        return False
    for b in bagmap[bag]:
        if b[0] == 'shiny gold' or shiny_gold(b[0]):
            return True
    return False

def how_many_bags(bag, bcount):
    if bag not in bagmap.keys() or len(bagmap[bag]) == 0:
        return 0
    for b in bagmap[bag]:
        bcount += int(b[1]) * (how_many_bags(b[0], 0) + 1)
    return bcount

c = list(filter(lambda x: shiny_gold(x), bagmap.keys()))
print(len(c))
print(how_many_bags('shiny gold', 0))