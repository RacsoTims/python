# URL: https://projecteuler.net/problem=46

# Problem: What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# n = p + 2 * s is the general form

import sys
sys.path.append("/home/oscar/python/")

import utils

primes = utils.get_primes()

for n in range(9, 6000, 2):
    
    goldbach = False
    
    if n in primes:
        continue
    else:
        s = 1
        while n - s**2 > 0:
            remainder = n - (2 * s**2)
            if remainder in primes:
                goldbach = True
                # print(f"{n} = {remainder} + {2} * {s}^{2}")
                break
            else:
                s += 1
    
    if not goldbach:
        print(n)
        break
