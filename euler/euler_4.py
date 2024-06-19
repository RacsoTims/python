# URL: https://projecteuler.net/problem=4

# Find the largest palindrome made from the product of two 3-digit numbers.

# check if input number is a palindrome
def palindrome(number):

    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


# test = 9009
# if palindrome(test):
#     print(f"{test} is een palindroom!")
# else:
#     print(f"{test} is geen palindroom!")
palindromes = []
iteration = 0

for x in range(100, 1000):
    for y in range(100 + iteration, 1000):

        candidate = x * y
        if palindrome(candidate):
            palindromes.append(candidate)
        else:
            continue

    iteration += 1  #1239 vs. 2470 - what explains the difference?

# print(len(palindromes), palindromes)
print(max(palindromes)) # The biggest palindrome is 906609, the product of 913 and 993
