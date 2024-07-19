# URL: https://projecteuler.net/problem=9

# PROBLEM: There exists exactly one Pythagorean triplet for which a+b+c = 1000
# Find the product abc

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

triplets = (utils.calculate_pythagoras(20))
perimeter = 1000    # see problem
divisors = utils.find_divisors(perimeter)

for triplet in triplets:
    if triplet[1] in divisors:
        multiplier = perimeter // triplet[1]
        product = 1
        for number in triplet[0]:
            product *= multiplier * number
        print(product)
        exit()
