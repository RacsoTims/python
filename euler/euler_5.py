# URL: https://projecteuler.net/problem=5

# PROBLEM: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

numbers = [n for n in range(1, 21)]
print(utils.calculate_kgvList(numbers))
