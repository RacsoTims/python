# URL: https://projecteuler.net/problem=43

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
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
