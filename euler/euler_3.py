# URL: https://projecteuler.net/problem=3

# OPDRACHT
# What is the largest prime factor of the number 600851475143?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

number = 600851475143   # zie opdracht
factorization = utils.prime_factorization(number)
print(factorization)
