# URL: https://projecteuler.net/problem=2

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

fibonacci = utils.get_fibonacci(including = 4000000)
even_sum = sum([n for n in fibonacci if n % 2 ==  0])
print(even_sum)
