# URL: https://projecteuler.net/problem=55

import sys
sys.path.append("/home/oscar/tools/")
import utils


def add_reverse(number) -> int:
    
    count = 0
    is_palindrome = False
    
    while count < 50:
        reverse = int(str(number)[::-1])
        if utils.check_ifPalindrome(sum((number, reverse))):
            is_palindrome = True
            break
        else:
            number += reverse
            count += 1
    
    return is_palindrome


lychrel = 0

for n in range(1, 10000):
    if add_reverse(n):
        continue
    else:
        lychrel += 1

print(lychrel)
