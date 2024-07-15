# URL: https://projecteuler.net/problem=50

import sys
sys.path.append("/home/oscar/tools/")

import utils

upper_bound = 1000000
primes = utils.get_primes(including = upper_bound)

largest_sums = []
length_sequences = []

for prime in primes:
    sums = [0]
    count = primes.index(prime)
    length = 0
    while sums[-1] < upper_bound:
        if count < len(primes):
            sums.append(sums[-1] + primes[count])
            count += 1
            length += 1
        else:
            break
    largest_sums.append(max([m for m in sums if m in primes]))
    length_sequences.append(length - 1)

for i in range(0, len(length_sequences)):
    if largest_sums[i+1] >= largest_sums[i]:
        largest_sum = largest_sums[i+1]
    else:
        break

print(largest_sum)
