# URL: https://projecteuler.net/problem=47

import sys
sys.path.append("/home/oscar/tools/")

import utils

sequence = 4

for n in range(3, 100000):
    for m in range(n, n+sequence):
        current = utils.prime_factorization(m).split(" * ")
        if len(current) == sequence and m != n+sequence-1:
            continue
        elif len(current) == sequence and m == n+sequence-1:
            for j in range(n, n+sequence):
                print(j)
            exit()
        else:
            break
