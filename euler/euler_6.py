# URL: https://projecteuler.net/problem=6

# OPDRACHT 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100 # zie opdracht
power = 2 # zie opdracht

sum_of_squares = 0
square_of_sum = 0

for x in range(1, limit + 1):

    sum_of_squares += x**power
    square_of_sum += x


answer = (square_of_sum**power) - sum_of_squares
print(answer)
