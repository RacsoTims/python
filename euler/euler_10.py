# URL: https://projecteuler.net/problem=10

# PROBLEM: Find the sum of all the primes below two million.

from sympy import isprime

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

prime_sum = 2
for n in range(3, 2000000, 2):
    if isprime(n):
        prime_sum += n

print(prime_sum)
