# URL: https://projecteuler.net/problem=34


from math import factorial

total_sum = 0
# check for successive ranges of powers of ten
for x in range(100000, 1000000):
    sum_factorials = 0
    split = [y for y in str(x)]

    for number in split:
        sum_factorials += factorial(int(number))
    
    if sum_factorials == x:
        print(x)
        total_sum += x

print(total_sum)
