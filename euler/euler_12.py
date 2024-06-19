# URL: https://projecteuler.net/problem=12

# OPDRACHT
# What is the value of the first triangle number to have over five hundred divisors?

import numpy as np

def generate_triangular(nth):

    triangle_number = (nth * (nth + 1)) / 2

    return check_divisors(triangle_number)


def check_divisors(triangle_number):

    count = 0
    for y in range(1, int(np.sqrt(triangle_number)) + 1):

        if triangle_number % y == 0:
            if y * y == triangle_number:
                count += 1
            else:
                count += 2

    return count


counter = 1
while(True):
    if generate_triangular(counter) <= 500:
        counter += 1
        continue
    else:
        result = int((counter * (counter + 1)) / 2)
        break

print(counter, result)
