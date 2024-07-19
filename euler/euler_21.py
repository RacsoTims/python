# URL: https://projecteuler.net/problem=21

# PROBLEM: Evaluate the sum of all the amicable numbers under 10,000.

import numpy as np
# (1) for a number, calculate the sum of its divisors (d(n)). (2) When done, store number and d(n) as (number, d(n))
# (3) Check if list of tuples contains a tuple (number1, d(n)1) such that number equals d(n)1 and d(n) equals number1
# (4) Store both numbers as (number, number1) in a different list

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils


start = 1
end = 10000 # see problem

numbers = [n for n in range(start, end)]
amicable = utils.check_ifAmicableList(numbers)

amicable_sum = 0
for pair in amicable:
    amicable_sum += sum(pair)
print(amicable_sum)
