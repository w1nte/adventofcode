import sys
import re


def play(deck1: list, deck2: list):
    c1 = deck1.pop(0)
    c2 = deck2.pop(0)

    if c1 > c2:
        deck1.append(c1)
        deck1.append(c2)
    elif c2 > c1:
        deck2.append(c2)
        deck2.append(c1)

    if len(deck1) == 0:
        return 2
    if len(deck2) == 0:
        return 1
    return 0


if __name__ == '__main__':
    input_content = sys.stdin.read()
    deck1, deck2 = [[int(n) for n in c.split('\n')] for c in re.findall(r'Player \d:\n(.+?)(?:\n\n|$)', input_content, re.DOTALL)]

    rounds = 0
    while True:
        rounds += 1
        result = play(deck1, deck2)
        if result > 0:
            print('Player {} won after {} rounds!'.format(result, rounds))

            score = 0
            winner_deck = deck1 if result == 1 else deck2
            for i in range(len(winner_deck)):
                score += winner_deck[i] * (len(winner_deck) - i)
            print('Score: {}'.format(score))
            break
