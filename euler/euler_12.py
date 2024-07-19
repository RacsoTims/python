# URL: https://projecteuler.net/problem=12

# PROBLEM: What is the value of the first triangle number to have over five hundred divisors?

from numpy import sqrt

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils


counter = 1
while True:
    if utils.find_divisorsAmount(utils.calculate_triangleNumber(counter)) <= 500:
        counter += 1
        continue
    else:
        result = utils.calculate_triangleNumber(counter)
        break

print(counter, result)
