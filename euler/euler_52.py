# URL: https://projecteuler.net/problem=52

import sys
sys.path.append("/home/oscar/tools/")
import utils

for n in range(100000, 1000000):
    check = [n * i for i in range(1, 7)]
    if utils.check_ifSameDigitsList(check):
        print(n)
        exit()
