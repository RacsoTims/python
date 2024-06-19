# URL: https://projecteuler.net/problem=20

# OPDRACHT
# Find the sum of the digits in the number 100!.

from math import factorial

result = sum(map(int, [x for x in str(factorial(100))]))
print(result)
