
with open('input1.txt', 'r') as f:
    numbers = f.read().split('\n')

    for x in range(0, len(numbers)):
        for y in range(x, len(numbers)):
            for z in range(y, len(numbers)):
                num1 = float(numbers[x])
                num2 = float(numbers[y])
                num3 = float(numbers[z])
                if (num1 + num2 + num3) == 2020:
                    print("{:.0f} * {:.0f} * {:.0f} = {:.0f}".format(num1, num2, num3, num1 * num2 * num3))