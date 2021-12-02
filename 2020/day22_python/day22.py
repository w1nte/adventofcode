import sys
import re


def copy_decks(deck1: list, deck2: list):
    return [[n for n in deck1], [n for n in deck2]]


def play_round(deck1: list, deck2: list):
    c1 = deck1.pop(0)
    c2 = deck2.pop(0)

    if len(deck1) >= c1 and len(deck2) >= c2:
        new_deck1, new_deck2 = [[n for i, n in enumerate(deck1) if i < c1], [n for i, n in enumerate(deck2) if i < c2]]
        winner = play_game(new_deck1, new_deck2)
    else:
        winner = 1 if c1 > c2 else 2

    if winner == 1:
        deck1.append(c1)
        deck1.append(c2)
    else:
        deck2.append(c2)
        deck2.append(c1)

    return winner


def play_game(deck1: list, deck2: list):
    round_decks = []
    while True:
        if len(deck1) == 0:
            return 2
        if len(deck2) == 0:
            return 1
        for prev_decks in round_decks:
            if deck1 == prev_decks[0] or deck2 == prev_decks[1]:
                return 1  # lul

        round_decks.append(copy_decks(deck1, deck2))
        play_round(deck1, deck2)


if __name__ == '__main__':
    input_content = sys.stdin.read()
    deck1, deck2 = [[int(n) for n in c.split('\n')] for c in re.findall(r'Player \d:\n(.+?)(?:\n\n|$)', input_content, re.DOTALL)]

    result = play_game(deck1, deck2)
    print('Player {} won!'.format(result))

    print(deck1, deck2)

    score = 0
    winner_deck = deck1 if result == 1 else deck2
    for i in range(len(winner_deck)):
        score += winner_deck[i] * (len(winner_deck) - i)
    print('Score: {}'.format(score))