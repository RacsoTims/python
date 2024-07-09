# URL: https://projecteuler.net/problem=46
# Problem: What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import sys
sys.path.append("/home/oscar/tools/")

import utils

primes = utils.generate_primes(3, 1000, 2)
goldbach = []

for n in range(9, 1000, 2): # nine is the smallest odd composite number
    if n in primes:
        continue
    else:
        for prime in primes:
            square = 1
            factor = 2 * square**2
            while n - prime - factor > 0:
                if n - prime - factor == 0:
                    is_goldbach = True
                    break
                else:
                    square += 1
                    factor = 2 * square**2
            if is_goldbach:
                break
            else:
                goldbach.append(n)
                break
    # else:
    #     square = 1
    #     factor = 2 * square**2
    #     while n - factor > 0:
    #         if n - factor in primes:
    #             goldbach.append(n)
    #             break
    #         else:
    #             square += 1
    #             factor = 2 * square**2

print(len(goldbach), goldbach)
