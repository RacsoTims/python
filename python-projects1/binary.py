from math import log, floor


def decimal2binary(number, length):
    digits = []
    for i in range(length, -1, -1):
        remainder = number - 2**i
        if remainder > 0:
            digits.append('1')
            number = remainder
        elif remainder == 0:
            digits.append('1')
            if i > 0:
                number = remainder
                continue
            else:
                return digits
        else:
            digits.append('0')
            if i == 0:
                return digits


lbound = int(input("Lower bound: "))
ubound = int(input("Upper bound: "))
ssize = int(input("Step size: "))

for number in range(lbound, ubound, ssize):
    length = floor(log(number, 2))
    zeros_and_ones = decimal2binary(number, length)
    print(f"{number} <-->", end=' ')
    n = 0
    m = 4
    while m < len(zeros_and_ones) + 4:
        print(''.join(zeros_and_ones[n:m]), end=' ')
        n += 4
        m += 4
    print(f"({len(zeros_and_ones)} bits)")
