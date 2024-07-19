# URL: https://projecteuler.net/problem=1

# FIND THE SUM OF ALL MULTIPLES OF 3 OR 5 BELOW 1000

# divisors: 3, 5

limit = 1000
multiples = [x for x in range(3, limit) if x % 3 == 0 or x % 5 == 0]

print(multiples)
print(len(multiples))
print(sum(multiples))
