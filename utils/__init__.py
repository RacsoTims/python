# Add the following in a script to import the modules below:

# LINUX:
# import sys
# sys.path.append("/home/oscar/python/")
# import utils

# WINDOWS:
# import sys
# sys.path.append("C:\\Users\\oscar\\my_stuff\\python")
# import utils


# ADD: twin primes, pythagoras, prime factorization pretty print, 


from math import sqrt, factorial
import numpy as np

from sys import platform


def determine_path():
    
    if platform == "win32":
        path = "C:\\Users\\oscar\\my_stuff\\python\\euler_data\\"
    elif platform == "linux":
        path = "/home/oscar/projects/python/euler_data/"
    
    return path

path = determine_path()


def remove_chars(text, rmv) -> str:
    
    for char in rmv:
        text = text.replace(char, "")
    
    return text


def generate_primes(start, end, step_size):
    
    primes = [2]
    
    for n in range(start, end, step_size):
        for prime in primes:
            if n % prime != 0:
                if prime == primes[-1]:
                    primes.append(n)
            else:
                break
    
    return primes


def store_primes():
    
    start = 3
    end = 1000000
    step_size = 2
    
    primes = generate_primes(start, end, step_size)
    
    with open(f'{path}primes.txt', 'w') as store:
        for prime in primes:
            if prime == primes[-1]:
                store.write(str(prime))
            else:
                store.write(str(prime) + ",")
    
    return True


def get_primes(quantity = False, including = False):
    
    primes = ""
    
    with open(f'{path}primes.txt', 'r') as data:
        for line in data.read():
            primes += line    
    
    primes = [int(x) for x in primes.split(",")]
    
    if quantity:
        primes = primes[:quantity]
    elif including:
        primes = [y for y in primes if y <= including]
    
    return primes


# takes as input a single integer and checks if the number is prime; returns a boolean
def check_ifPrime(number):
    
    is_prime = False
    
    if number % 2 == 0:
        return is_prime
    else:
        primes = get_primes(including = number)
    
    if number == primes[-1]:
        is_prime = True
    
    return is_prime


# takes as input a list of integers; returns a sublist of integers that are prime
def check_ifPrimeList(numbers) -> list:
    
    primes = get_primes(including = max(numbers))
    result = [x for x in numbers if x in primes]
    
    return result


def prime_factorization(number):
    
    factorization = []
    primes = get_primes(including = number)
    
    if number == primes[-1]:
        factorization.append((number, 1))
    else:
        for prime in primes:
            count = 0
            while number % prime == 0:
                number //= prime
                count += 1
            if count == 1:
                factorization.append((prime, 1))
            elif count > 1:
                factorization.append((prime, count))
            if number == 1:
                break
    
    return factorization


# takes as input a pair of integers (list or tuple) and checks if they are coprime; returns a boolean
def check_ifCoprime(pair):
    
    is_coprime = False
    divisors0 = find_divisors(pair[0])
    divisors1 = find_divisors(pair[1])
    
    for divisor in divisors0:
        if divisor == 1:
            continue
        elif divisor not in divisors1:
            if divisor == divisors0[-1]:
                is_coprime = True
        else:
            break
    
    return is_coprime


# takes as input an integer and finds its (proper) divisors; returns a list of divisors
def find_divisors(number, proper = False):
    
    if not proper:
        divisors = [1, number] if number != 1 else [1]
    else:
        divisors = [1]
    
    for n in range(2, int(sqrt(number)) + 1):
        if number % n == 0 and n**2 != number:
            divisors.append(n)
            multiplier = number // n
            divisors.append(multiplier)
        elif number % n == 0 and n**2 == number:
            divisors.append(n)
    
    divisors.sort()
    
    return divisors


def check_ifAmicable(pair) -> tuple:
    
    is_amicable = False
    su1 = sum(find_divisors(pair[0], proper = True))
    su2 = sum(find_divisors(pair[1], proper = True))
    
    if pair[0] == su2 and pair[1] == su1:
        is_amicable = True
    
    return is_amicable


def check_ifAmicableList(numbers) -> list:
    
    amicable = []
    
    for number in numbers:
        su1 = sum(find_divisors(number, proper = True))
        su2 = sum(find_divisors(su1, proper = True))
        if number == su2 and su1 != number and (su1, number) not in amicable:
            amicable.append((number, su1))
    
    return amicable


def find_divisorsAmount(number) -> int:
    
    divisors = find_divisors(number)
    
    return len(divisors)


def check_ifPandigital(number, zero = False) -> str:
    
    is_pandigital = False
    
    if zero:
        digits = [n for n in range(0, len(number))]
    else:
        digits = [n for n in range(1, len(number) + 1)]
    
    for digit in number:
        if int(digit) in digits:
            digits.pop(digits.index(int(digit)))
    
    if len(digits) == 0:
        is_pandigital = True
    
    return is_pandigital


def count_uniqueDigits(digits) -> list:
    
    unique = []
    
    for i in range(0, len(digits)):
        digit = digits[i]
        if digit not in digits[0:i] and digit not in digits[i+1:]:
            unique.append(digit)
    
    return len(unique)


def calculate_nck(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def generate_permutations(digits) -> list:
    
    permutations = []    
    unique = count_uniqueDigits(digits)
    
    if unique == len(digits) and 0 not in digits:
        count = factorial(len(digits))
    elif unique == len(digits) and 0 in digits:
        count = factorial(len(digits)) - factorial(len(digits) - 1)
    else:
        count = calculate_nck(len(digits), unique)
    
    while len(permutations) < count:
        new_digits = digits[:]
        np.random.shuffle(new_digits)
        if new_digits not in permutations and new_digits[0] != 0:
            permutations.append(new_digits)
            reverse = new_digits[::-1]
            if reverse[0] != 0:
                permutations.append(new_digits[::-1])
    
    return permutations


def get_orderedPermutations(permutations) -> list:
    
    ordered = []
    
    for permutation in permutations:
        ordered.append(int("".join([str(x) for x in permutation])))
    ordered.sort()
    
    return ordered


def calculate_pythagoras(quantity, irreducible = False):
    
    triplets = []
    sequence = [n**2 for n in range(1, 3000)]
    
    for i in range(0, len(sequence)):
        a = sequence[i]
        for j in range(i + 1, len(sequence)):
            b = sequence[j]
            if irreducible:
                coprime = check_ifCoprime((a, b))
                if not coprime:
                    continue
            c = a + b
            if c in sequence:
                perimeter = int(sum((i+1, j+1, sequence.index(c) + 1)))
                triplet = (i+1, j+1, int(sqrt(c)))
                triplets.append((triplet, perimeter))
                break
        if len(triplets) < quantity:
            continue
        else:
            break
    
    return triplets


def generate_fibonacci(quantity = False, limit = False):
    
    sequence = [1, 2]
    
    if quantity:
        while quantity - 2 > 0:
            next_term = sum(sequence[(len(sequence) - 2):len(sequence)])   # the last two entries in 'sequence' are summed to get the next term
            sequence.append(next_term)
            quantity -= 1
    if limit:
        while sum(sequence[(len(sequence) - 2):len(sequence)]) <= limit:
            next_term = sum(sequence[(len(sequence) - 2):len(sequence)])
            sequence.append(next_term)
    
    return sequence


def store_fibonnaci():
    
    fibonacci = generate_fibonacci(quantity = 100)
    
    with open(f'{path}fibonacci.txt', 'w') as store:
        for term in fibonacci:
            if term == fibonacci[-1]:
                store.write(str(term))
            else:
                store.write(str(term) + ",")
    
    return True


def get_fibonacci(quantity = False, including = False):
    
    fibonacci = ""
    
    with open(f'{path}fibonacci.txt', 'r') as data:
        for line in data.read():
            fibonacci += line    
    
    fibonacci = [int(x) for x in fibonacci.split(",")]
    
    if quantity:
        fibonacci = fibonacci[:quantity]
    elif including:
        fibonacci = [y for y in fibonacci if y <= including]
    
    return fibonacci


def check_ifPalindrome(number):
    
    is_palindrome = False
    
    if str(number) == str(number)[::-1]:
        is_palindrome = True
    
    return is_palindrome


def calculate_ggd(pair) -> tuple:   # 'ggd' = grootste gemeenschappelijke deler
    
    divisors0 = find_divisors(pair[0])
    divisors1 = find_divisors(pair[1])    
    ggd = max([n for n in divisors0 if n in divisors1])
    
    return ggd


def calculate_kgv(pair) -> tuple:
    
    return pair[0] * pair[1] // calculate_ggd(pair)


def calculate_kgvList(numbers) -> list:   # 'kgv' = kleinste gemeenschappelijke veelvoud
    
    kgv = 1
    
    for i in range(0, len(numbers)):
        kgv *= numbers[i]
    
    factors = prime_factorization(kgv)
    for factor in factors:
        power = factor[1]
        while factor[0] ** power > max(numbers):
            kgv //= factor[0]
            power -= 1
    
    return kgv


def calculate_triangleNumber(number):
    
    return number*(number + 1) // 2


def collatz_sequence(number):
    
    terms = 1
    
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        
        terms += 1
    
    return terms


# check = store_primes()
# if check:
#     print("Success!")

# check = store_fibonnaci()
# if check:
#     print("Success!")
