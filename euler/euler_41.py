# URL: https://projecteuler.net/problem=41

import sys
sys.path.append("/home/oscar/tools/")

import utils

check = [x for x in range(3, 987654 + 1) if x % 2 != 0] # 9876; 98765; 987654; 9876543; 98765432; 987654321
primes = utils.check_ifPrimeList(check)
pandigital_primes = []

for prime in primes:
        is_pandigital = utils.check_ifPandigital(str(prime))
        if is_pandigital:
                pandigital_primes.append(prime)

print(pandigital_primes)
print(max(pandigital_primes))
