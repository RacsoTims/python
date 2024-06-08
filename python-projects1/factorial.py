"""
Author: O. Smit

Description:

Calculates the factorial of any positive integer n,
or the choose function for any positive integers
n and k
"""


def factorial(number, result):
    for factor in range(2, number + 1):
        result *= factor
    return result


def n_choose_k(n, k, result):
    x = factorial(n, result)
    y = factorial(k, result)
    z = factorial((n - k), result)
    w = x / (y * z)
    return w


# start = 1

# print("Do you want the factorial of n (1)\
#  or the choose function for n and k (2)?")
# choice = input("> ")
# if choice == "1":
#     n = int(input("Value of n: "))
#     answer = factorial(n, start)
#     print(f"Your answer: {answer}.")
# if choice == "2":
#     n = int(input("Value of n: "))
#     k = int(input("Value of k: "))
#     answer = n_choose_k(n, k, start)
#     print(f"Your answer: {answer}.")
