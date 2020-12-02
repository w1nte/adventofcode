from day2a import parse_database_line


if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        database = f.read().split('\n')
        passwords_total = len(database)
        passwords_valid = 0
        for line in database:
            first_char, second_char, char, passw = parse_database_line(line)

            if (char == passw[int(first_char)-1] or char == passw[int(second_char)-1]) and passw[int(first_char)-1] != passw[int(second_char)-1]:
                passwords_valid += 1

        print("Passwords total: {}, Passwords valid: {}".format(passwords_total, passwords_valid))