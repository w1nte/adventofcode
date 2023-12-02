import sys, re

lines = [re.search("^Game (\d+): (.*)", line).groups()[0:] for line in sys.stdin]
games = [(int(line[0]), list(map(lambda x: list(map(lambda y: re.search('(\d+) ([a-zA-Z]+)', y).groups(), x.split(','))), line[1].split(';')))) for line in lines]
games = [(game[0], [{color: int(num) for num, color in round} for round in game[1]]) for game in games]
filtered = [game[0] for game in games if all([(round.get('red', 0)<= 12 and round.get('green', 0) <= 13 and round.get('blue', 0) <= 14) for round in game[1]])]

print(sum(filtered))