# URL: https://projecteuler.net/problem=4

# Find the largest palindrome made from the product of two 3-digit numbers.

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")

import utils

palindromes = []
iteration = 0

for x in range(100, 1000):
    for y in range(100 + iteration, 1000):
        
        candidate = x * y
        if utils.check_ifPalindrome(candidate):
            palindromes.append(candidate)
        
    iteration += 1  #1239 vs. 2470 - what explains the difference?

# print(len(palindromes), palindromes)
print(max(palindromes)) # The biggest palindrome is 906609, the product of 913 and 993
print(utils.find_divisors(max(palindromes)))
