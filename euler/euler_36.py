# URL: https://projecteuler.net/problem=36


def convert_binary(number, base):
    bin = ""
    while number >= base:
        remainder = number % base
        number //= base
        bin += str(remainder)
    else:
        bin += str(number)
    bin = bin[::-1]
    return bin


def check_ifpalindrome(number, base):
    if str(number) == str(number)[::-1]:
        bin = convert_binary(number, base)
        if bin == bin[::-1]:
            palindromic = True
        else:
            palindromic = False
    else:
        palindromic = False
    return palindromic


start = 1
end = 1000000   # see the assignment on the euler website
step_size = 2   # an even number in binary cannot be a palindrome (if you exclude leading zeros)
base = 2
palindrome_sum = 0

for x in range(start, end, step_size):
    if check_ifpalindrome(x, base):
        print(x)
        palindrome_sum += x

print(palindrome_sum)
