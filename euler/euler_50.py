# URL: https://projecteuler.net/problem=50

import sys
sys.path.append("/home/oscar/python/")

import utils

upper_bound = 1000000
primes = utils.get_primes(including = upper_bound)

prime_sum = 0
length = 0
sequence = []

for i in range(0, len(primes) - 1):
    
    temp = 0    # here we will store the sum of a particular sequence
    temp1 = 0   # here we will store the length of a sequence
    temp2 = []  # here we will store the consecutive primes that make up a sequence
    iteration = i
    
    while temp < upper_bound:
        temp += primes[iteration]
        temp2.append(primes[iteration])
        iteration += 1
        temp1 += 1
        if temp1 > length and temp in primes:
            prime_sum = temp
            length = temp1
            sequence = temp2

print(sequence, prime_sum, length + 1)
