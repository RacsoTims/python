# URL: https://projecteuler.net/problem=56

import sys
sys.path.append("/home/oscar/tools/")
import utils

maximum_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        if utils.digit_sum(a**b) > maximum_digital_sum:
            maximum_digital_sum = utils.digit_sum(a**b)

print(maximum_digital_sum)
