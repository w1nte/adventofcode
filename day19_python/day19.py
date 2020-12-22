import sys
import re


def test_rule(rules, rule, text):
    if len(text) == 0:
        return 0

    for seq in rules[rule]:
        if len(seq) == 1 and isinstance(seq[0], str):  # is a
            return 1 if text[0] == seq[0] else 0

        p = 0
        seqc = True
        for next_rule in seq:
            np = test_rule(rules, next_rule, text[p:])
            if np == 0:
                seqc = False
                break
            p += np
        if not seqc:
            continue
        return p
    return 0


def test(rules, rule, text):
    return test_rule(rules, rule, text) == len(text)


if __name__ == '__main__':
    input_content = sys.stdin.read()
    rules = {int(r[0]): [[(int(a) if a.isnumeric() else a[1]) for a in n.split(" ")] for n in r[1].split(" | ") ] for r in re.findall(r'^(\d+): (.*)', input_content, re.MULTILINE)}
    input_text = re.findall(r'^[a-z]+', input_content, re.MULTILINE)

    print(sum([test(rules, 0, t) for t in input_text]))