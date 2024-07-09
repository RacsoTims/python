# URL: https://projecteuler.net/problem=40

# A formula for finding the nth digit of Champernowne's Constant (1234567891011...)

digits = [1, 10, 100, 1000, 10000, 100000, 1000000] # see the assignment on euler website
answer = 1

for digit in digits:
    nth_digit = digit
    magnitude = 1
    number = 0
    result = 0
    
    while nth_digit > 9 * magnitude * 10**(magnitude - 1):
        nth_digit -= 9 * magnitude * 10**(magnitude -1 )
        number += 9 * 10**(magnitude -1)
        magnitude += 1
    
    while nth_digit > magnitude:
        nth_digit -= magnitude
        number += 1
    
    result = str(number + 1)[nth_digit - 1]
    answer *= int(result)
    print(result)

print(answer)
