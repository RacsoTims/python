# URL: https://projecteuler.net/problem=48

def calculate_lastDigit(number, power):
    last_digit = str(number)[-1]
    while power > 1:
        last_digit = str((int(last_digit) * number))[-1]
        power -= 1
    return last_digit

number = 27
power = 18
test = calculate_lastDigit(number, power)
print(f"{number}^{power} ends in: {test}")
