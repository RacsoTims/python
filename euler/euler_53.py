# URL: https://projecteuler.net/problem=53

import sys
sys.path.append("/home/oscar/tools/")
import utils

counter = 0

for n in range(23, 101): # see problem
    for k in range(1, n+1):
        if utils.calculate_nck(n, k) > 1000000:
            counter += 1

print(counter)
