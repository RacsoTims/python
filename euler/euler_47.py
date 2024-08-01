# URL: https://projecteuler.net/problem=47

import sys
sys.path.append("/home/oscar/tools/")

import utils

factors = 4
found = 0
number = 134000

while found < factors:
    temp = 0
    if len(utils.prime_factorization(number)) == factors:
        temp += 1
        for n in range(number+1, number+factors):
            if len(utils.prime_factorization(n)) == factors:
                temp += 1
            else:
                break
    if temp == factors:
        break
    else:
        number += 1

for m in range(number, number+factors):
    print(m)
    print(utils.prime_factorizationPrettyPrint(m))
