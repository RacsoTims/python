# URL: https://projecteuler.net/problem=23

# PROBLEM: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import sys
sys.path.append("/home/oscar/tools/")

import utils


def check_ifabundant(number, divisors):
    
    is_abundant = False
    
    if sum(divisors) > number:
        is_abundant = True
    
    return is_abundant


abundant = []
for n in range(2, 28123 + 1):   # 'By mathematical analysis, it can be shown that all integers greater than 23183 can be written as the sum of two abundant numbers.'
    divisors = utils.find_divisors(n, proper = True)
    is_abundant = check_ifabundant(n, divisors)
    if is_abundant:
        abundant.append(n)
    else:
        continue

# print(len(abundant), abundant)

not_sum = []    # list of numbers that cannot be written as the sum of two abundant numbers
for m in range(1, 23183 + 1):
    is_not_sum = False
    check = [x for x in abundant if x <= m - 12] if m > 12 else []
    if not check:
        not_sum.append(m)
    else:
        for number in check:
            remainder = m - number
            if remainder in check:
                break
            elif remainder not in check and number == check[-1]:
                is_not_sum = True
        if is_not_sum:
            not_sum.append(m)

print(sum(not_sum), not_sum)
