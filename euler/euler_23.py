# URL: https://projecteuler.net/problem=23

# OPDRACHT
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import numpy as np
abundant = []
deficient = []
perfect = []

not_sum_abundant = []


def check_abundance(number, divisor_sum):
    if divisor_sum > number:
        return True
    elif divisor_sum < number:
        return False
    else:
        return "perfect"


def calculate_sum_proper_divisors(number):

    su = 0
    for x in range(1, int(np.sqrt(number)) + 1):
        temp = number % x
        if temp == 0:
            complement = number // x
            if x != 1:
                su += x + complement if x*x != number else x
            else:
                su += x
    return (check_abundance(number, su))


end = 23124 # zie opdracht

for x in range(2, end):
    result = calculate_sum_proper_divisors(x)
    if result and result != "perfect":
        abundant.append(x)

for y in range(16001, end):
    if y < 23:
        not_sum_abundant.append(y)
    elif y in abundant:
        continue
    else:
        cut = (len(abundant) // 2) + 1
        # print(y)
        for number in abundant[:cut]:
            # print(y)
            if (y - number) in abundant:
                break
            elif (y - number) not in abundant and number == abundant[-1]:
                not_sum_abundant.append(y)
                print(not_sum_abundant)
            # else:
            #     continue


# print(abundant, len(abundant))
print(not_sum_abundant, end)