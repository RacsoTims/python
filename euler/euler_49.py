# URL: https://projecteuler.net/problem=49

import sys
sys.path.append("/home/oscar/tools/")

import utils

# get all prime numbers bigger than 1000 and lower than 10000
temp = utils.get_primes(including = 10000)
primes = [n for n in temp if n > 1000]

trio = []
found = False

for prime in primes[259:260]:
    digits = [int(x) for x in str(prime)]
    permutations = [p for p in utils.get_orderedPermutations(utils.generate_permutations(digits)) if p in primes]
    if len(permutations) >= 3:
        for i in range(1, len(permutations)):
            for j in range(0, i):
                difference = permutations[i] - permutations[j]
                check = permutations[i] + difference
                if difference < 1000 or check > 10000:
                    continue
                elif check in permutations:
                    sequence = (permutations[j], permutations[i], check, difference)
                    if sequence not in trio:
                        trio.append(sequence)
                        print(permutations)
                    # found = True
    if found:
        break

print(trio)
