import re

import sys
sys.path.append("/home/oscar/tools/")

import utils

test = (13, 18)
print(utils.find_divisors(test[0]))
print(utils.find_divisors(test[1]))

if utils.check_ifCoprime(test):
    print(f"{test[0]} and {test[1]} are coprime.")
else:
    print(f"{test[0]} and {test[1]} are NOT coprime.")
