# URL: https://projecteuler.net/problem=21

# OPDRACHT
# Evaluate the sum of all the amicable numbers under 10,000.

import numpy as np
# (1) for a number, calculate the sum of its divisors (d(n)). (2) When done, store number and d(n) as (number, d(n))
# (3) Check if list of tuples contains a tuple (number1, d(n)1) such that number equals d(n)1 and d(n) equals number1
# (4) Store both numbers as (number, number1) in a different list

tuples = []
amicables = []


def check_if_amicable(tuples, amicables):

    for tuple in tuples:
        x, y = tuple
        if tuple[::-1] in tuples and tuple != (x,x) and tuple[::-1] not in amicables:
            amicables.append(tuple)
    return amicables


def calculate_sum_proper_divisors(start, end, tuples):

    for number in range(start, end + 1):
        su = 0
        for x in range(1, int(np.sqrt(number)) + 1):
            temp = number % x
            if temp == 0:
                complement = number // x
                if x != 1:
                    su += x + complement if x*x != number else x
                else:
                    su += x
        tuple = (number, su)
        tuples.append(tuple)
    return check_if_amicable(tuples, amicables)


def calc_pair_sum(amicables):
    amicable_sum = 0
    for pair in amicables:
        amicable_sum += sum(pair)
    return amicable_sum


start = 1
end = 10000 # zie opdracht

result = calculate_sum_proper_divisors(start, end, tuples)
answer = calc_pair_sum(result)
print(f"Sum: {answer}\t{result}")
