# URL: https://projecteuler.net/problem=27

import sys
sys.path.append("/home/oscar/python/")

import utils

max_length = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        prime = n**2 + a*n + b
        primes = []
        while utils.check_ifPrime(prime):
            primes.append(prime)
            n += 1
            prime = n**2 + a*n + b
        if len(primes) > max_length:
            max_length = len(primes)
            product = a * b
            # print(a, b, len(primes), primes)

print(max_length, product)
