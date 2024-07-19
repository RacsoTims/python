# URL: https://projecteuler.net/problem=7

# OPDRACHT
# What is the 10001st prime number?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

result = utils.get_primes(quantity = 10001)
print(result[-1])
