
with open('input1.txt', 'r') as f:
    numbers = f.read().split('\n')

    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            num1 = float(numbers[i])
            num2 = float(numbers[j])
            if (num1 + num2) == 2020:
                print("{:.0f} * {:.0f} = {:.0f}".format(num1, num2, num1 * num2))