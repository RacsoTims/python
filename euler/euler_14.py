# URL: https://projecteuler.net/problem=14

# PROBLEM: Which starting number, under one million, produces the longest [Collatz] chain?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

chains = [1]
upper_bound = 1000000 # see problem

for x in range(2, upper_bound):
    sequence_length = utils.collatz_sequence(x)
    if sequence_length > chains[0]:
        chains[0] = sequence_length
        longest = x

print(longest)
