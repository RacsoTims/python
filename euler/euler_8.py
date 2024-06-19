# URL: https://projecteuler.net/problem=8

# OPDRACHT
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# takes as input a string and returns the SUM of its digits
def calc_sum(substring):

    add = 0
    for char in substring:
        add += int(char)
    return add


# takes as input a string and returns the PRODUCT of its digits
def calc_product(substring):

    multiply = 1
    for char in substring:
        multiply *= int(char)
    return multiply


content = open("/home/oscar/Downloads/euler_8.txt", "r")

# remove trailing newlines
digits = (content.read()).replace("\n", "")

adjacent = 13 # zie opdracht
start = 0

max_sum = 0

for digit in digits:

    end = start + adjacent

    group = digits[start:end]
    group_sum = calc_sum(group)

    if group_sum > max_sum:
        max_sum = group_sum

        if "0" not in group:
            max_product = calc_product(group)

    else:
        start += 1
        continue
    
    start += 1
print(max_sum) # should be 35 (9+9+8+9) # edit: IT IS! :)
print(max_product)
