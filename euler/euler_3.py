# URL: https://projecteuler.net/problem=3

# OPDRACHT
# What is the largest prime factor of the number 600851475143?

import numpy as np
# from ..primes_onemoretime import generate_primes


def generate_primes(start, end, step_size):

    primes = [2]
    for n in range(start, end, step_size):
        for prime in primes:
            if n % prime != 0:
                if prime == primes[-1]:
                    primes.append(n)
            else:
                break
    return primes


start = 3
end = 10000
step_size = 2
primes = generate_primes(start, end, step_size)

number = 600851475143   # zie opdracht
factorization = []

for prime in primes:
    x = number
    count = 0
    while x % prime == 0:
        count += 1
        x /= prime

    if count > 0:
        factorization.append(f"{prime}^{count}")

    if x == 1:
        break

print(f"{number}:", end=" ")
for prime_factor in factorization:
    if prime_factor != factorization[-1]:
        print(f"{prime_factor}", end=" ")
    else:
        print(prime_factor)
print(f"Largest prime factor: {factorization[-1]}")
