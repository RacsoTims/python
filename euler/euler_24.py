# URL: https://projecteuler.net/problem=24

# OPDRACHT
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial
permutation = ""
nth_permutation = 1000000 # zie opdracht

for x in range(9, -1, -1):
    iteration = 0
    temp = 0
    while temp < nth_permutation:
        if temp + factorial(x) > nth_permutation:
            break
        else:
            temp += factorial(x)
            iteration += 1
    nth_permutation -= temp
    if str(iteration) not in permutation:
        permutation += str(iteration)
        # print(permutation)
    else:
        temp1 = 1
        # print(iteration, permutation)
        while str((iteration + temp1)) in permutation:
            temp1 += 1
        permutation += str(iteration + temp1)


print(f"The {10**6}th permutation is: {permutation}")
