# URL: https://projecteuler.net/problem=43

import sys
sys.path.append("/home/oscar/tools/")
import utils

divisors = [2, 3, 5, 7, 11, 13, 17] # see problem
number = "1406357289"

iteration = 0
for i in range(1, len(number) - 2):
    trio = "".join(number[i:i+3])
    if int(trio) % divisors[iteration] == 0:
        divisibility = True
    else:
        divisibility = False
    iteration += 1

if divisibility:
    print(number)

for m in range(100, 1000, 2):
    # print(m)
    if m % 2 == 0 and utils.check_ifRepeats(str(m)):
        digits = [n for n in range(0, 10)]
        
        print(m)
