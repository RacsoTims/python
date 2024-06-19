# URL: https://projecteuler.net/problem=16

# OPDRACHT
# What is the sum of the digits of the number 2**1000?

# Algoritme
# Je gaat van achter naar voren door het getal. Elk cijfer (x) verdubbel je.

# Als een verdubbeling boven de tien uitkomt schrijf je 2x % 10 op de plek van het cijfer dat je verdubbelt.

# (2x - (2x % 10)) / 10 onthoud je er tel je op bij het volgende cijfer NA diens verdubbeling.
# Herhaal tot je alle cijfers van het getal hebt gehad.


def calculate_nthPower(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        current = base
        n = 2
        while n <= power:
            current = multiplication(current, base)
            n += 1
    return current


def multiplication(current, factor):
    digits = [x for x in str(current)]
    digits_new = []
    carry = [0]
    iteration = 0

    for digit in digits[::-1]:

        temp = factor * int(digit)
        if temp + carry[0] >= 10 and iteration != len(digits) - 1:
            carry_units = carry[0] % 10
            carry_remaining_digit = int((carry[0] - carry_units) / 10)

            digit_new = (temp + carry_units) % 10
            digits_new.insert(0, digit_new)

            carry_over = int((temp + carry_units - digit_new) / 10)
            carry[0] = carry_over + carry_remaining_digit

        elif iteration == len(digits) - 1:
            digit_new = temp + carry[0]
            digits_new.insert(0, digit_new)

        elif temp + carry[0] <= 9:
            digits_new.insert(0, temp+carry[0])
            carry[0] = 0

        iteration += 1
    return int("".join(list(map(str, digits_new))))


def calc_digit_sum(number):
    su = []
    for digit in str(number):
        su.append(int(digit))
    return sum(su)


base = 2 # zie opdracht
power = 1000 # zie opdracht

result = calc_digit_sum(calculate_nthPower(base, power))
print(f"{base}^{power}={calculate_nthPower(base, power)}\nSum of digits: {result}")
