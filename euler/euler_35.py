# URL: https://projecteuler.net/problem=35

import sys
sys.path.append("/home/oscar/tools/")

import utils


def generate_rotations(number):
    
    rotations = [number]
    length = len(str(number))
    
    for x in range(0, length -1):
        last_digit = number % 10
        number = last_digit * pow(10, length - 1) + ((number - last_digit) // 10)
        rotations.append(number)
    
    if len(rotations) == length:
        return rotations


def check_ifcircular(primes):
    
    circular_primes = [2]
    evens = [0, 2, 4, 6, 8] # any number that contains an even digit cannot be a circular prime
    for prime in primes:        
        contains_evendigit = False        
        for even_digit in evens:
            if str(even_digit) in str(prime):
                contains_evendigit = True
                break
        if contains_evendigit:
            continue
        else:
            numbers = generate_rotations(prime)
            for j in range(0, len(numbers)):
                if numbers[j] in primes:
                    if j == len(numbers) - 1:
                        circular_primes.append(prime)
                else:
                    break
    return circular_primes


start = 3
end = 1000000   # zie opdracht
step_size = 2   # except for the number two, no even number can be prime

# primes = utils.generate_primes(start, end, step_size)
# result = check_ifcircular(primes)

# print(len(result), result)
print(utils.check_ifprime(3))
print(utils.check_ifprime_range([11, 12, 13, 14, 15, 16, 17, 18, 19]))
