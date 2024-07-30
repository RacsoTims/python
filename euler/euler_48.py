# URL: https://projecteuler.net/problem=48

# PROBLEM: Find the last ten digits of the series, 1^2 + 2^2 + 3^3 + ... + 1000^1000.


def calculate_lastDigit(number, power, end):
    last_digit = str(number)[-end::]
    while power > 1:
        last_digit = str((int(last_digit) * number))[-end::]
        power -= 1
    return last_digit


end = 10    # see problem
series = []

for number in range(1, 10001):
    last_digits = calculate_lastDigit(number, number, end)
    series.append(int(last_digits))
    # print(f"{number}^{power} ends in: {test}")

answer = str(sum(series))[-end::]
print(answer)
