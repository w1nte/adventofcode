import sys, re
from functools import reduce

lines = [re.search("^Game (\d+): (.*)", line).groups()[0:] for line in sys.stdin]
games = [(int(line[0]), list(map(lambda x: list(map(lambda y: re.search('(\d+) ([a-zA-Z]+)', y).groups(), x.split(','))), line[1].split(';')))) for line in lines]

games = [(game[0], [{color: int(num) for num, color in round} for round in game[1]]) for game in games]
min = [(game[0], reduce(lambda a, b: {i: max(a.get(i, 0), b.get(i, 0)) for i in set(a).union(b)},game[1])) for game in games]
power = [reduce(lambda x,y: x*y, game[1].values()) for game in min]

print(sum(power))