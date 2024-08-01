# URL: https://projecteuler.net/problem=60

import sys
sys.path.append("/home/oscar/tools/")
import utils


def concatenate(subset) -> list:
    
    concatenated = []
    
    for i in range(0, len(subset)):
        for j in range(i + 1, len(subset)):
            concatenated.append(int(str(subset[i]) + str(subset[j])))
            concatenated.append(int(str(subset[j]) + str(subset[i])))
    
    return concatenated


def check_primes(concatenated, primes) -> bool:
    
    all_prime = True
    
    for number in concatenated:
        if number not in primes:
            all_prime = False
            break
    
    return all_prime


primes = utils.get_primes()

for prime in primes:
    
    subset = [3, 7, 109, 673]
    
    if prime not in subset:
        subset.append(prime)
        check = check_primes(concatenate(subset), primes)
    else:
        continue
    
    if check:
        print(subset)
        print(concatenate(subset), len(concatenate(subset)))
        break
