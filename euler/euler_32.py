# URL: https://projecteuler.net/problem=32

import sys
sys.path.append("/home/oscar/tools/")

import utils

sum = 0
products = []

for multiplicand in range(1, 10000):
    for multiplier in range(multiplicand + 1, 10000):
        product = multiplicand * multiplier
        length = len(str(multiplicand)) + len(str(multiplier)) + len(str(product))
        
        if length == 9:
            concatenated = str(multiplicand) + str(multiplier) + str(product)
            pandigital = utils.check_ifPandigital(concatenated)
            if pandigital and product not in products:
                sum += product
                products.append((product))
                print(product, multiplicand, multiplier)
            else:
                continue
        else:
            continue

print(sum, products)
