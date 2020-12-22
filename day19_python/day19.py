import sys
import re


def test_rule_8_and_11(rules, text):
    # rule 8: 42 | 42 8
    r = test_rule(rules, 42, text)
    if r == 0:
        return 0
    t = r
    t42 = 0
    while True:
        r = test_rule(rules, 42, text[t:])
        if r == 0:
            break
        t += r
        t42 += 1

    # rule 11: 42 31 | 42 11 31
    r = test_rule(rules, 31, text[t:])
    if r == 0:
        return 0
    t += r
    for i in range(t42-1):
        r = test_rule(rules, 31, text[t:])
        if r == 0:
            return t
        t += r
        if t == len(text):
            return t
    return t


def test_rule(rules, rule, text):
    if len(text) == 0:
        return 0
    for seq in rules[rule]:
        if len(seq) == 1 and isinstance(seq[0], str):  # is a
            return 1 if text[0] == seq[0] else 0

        p = 0
        seqb = False
        for next_rule in seq:
            np = test_rule(rules, next_rule, text[p:])
            if np <= 0:
                seqb = True
                break
            p += np
        if seqb:
            continue
        return p
    return 0


if __name__ == '__main__':
    input_content = sys.stdin.read()
    rules = {int(r[0]): [[(int(a) if a.isnumeric() else a[1]) for a in n.split(" ")] for n in r[1].split(" | ") ] for r in re.findall(r'^(\d+): (.*)', input_content, re.MULTILINE)}
    input_text = re.findall(r'^[a-z]+', input_content, re.MULTILINE)

    # part 1
    print(len([t for t in input_text if test_rule(rules, 0, t) == len(t)]))

    # part 2
    print(len([t for t in input_text if test_rule_8_and_11(rules, t) == len(t)]))