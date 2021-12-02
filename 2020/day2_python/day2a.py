import re

def parse_database_line(line):
    parsed = re.findall('(\d+)-(\d+) (\S+): (.+)', line)
    if len(parsed) < 0:
        raise Exception("parsing of line failed")
    return parsed[0]

def count_chars(str, char):
    counter = 0
    for c in str:
        if c == char:
            counter += 1
    return counter


if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        database = f.read().split('\n')
        passwords_total = len(database)
        passwords_valid = 0
        for line in database:
            cmin, cmax, c, passw = parse_database_line(line)
            chars = count_chars(passw, c)
            if int(cmin) <= chars <= int(cmax):
                passwords_valid += 1

        print("Passwords total: {}, Passwords valid: {}".format(passwords_total, passwords_valid))