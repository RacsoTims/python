# URL: https://projecteuler.net/problem=41

from sympy import isprime

import sys
sys.path.append("/home/oscar/python/")

import utils

size = 7
digits = [n for n in range(1, size + 1)]
temp = utils.get_orderedPermutations(utils.generate_permutations(digits))
# print(len(pandigitals))

# get rid of even numbers
pandigitals = []
for pandigital in temp:
        if pandigital % 2 == 0:
                continue
        else:
                pandigitals.append(pandigital)
pandigitals.sort(reverse=True)

pandigital_primes = []
for number in pandigitals:
        if isprime(number):
                print(number)
                exit()
# for prime in primes:
#         is_pandigital = utils.check_ifPandigital(str(prime))
#         if is_pandigital:
#                 pandigital_primes.append(prime)

# print(pandigital_primes)
# print(max(pandigital_primes))
