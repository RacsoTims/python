from math import sqrt, pi
from prime_numbers import PrimeNumberGenerator
import numpy as np


def generate_primes():
    primes = PrimeNumberGenerator(3, 300, 2)
    list_of_primes = primes.prime_number_generator()
    return list_of_primes


def generate_squares(lower_bound, upper_bound):
    list_of_squares = []
    for i in range(lower_bound, upper_bound):
        list_of_squares.append(i**2)
    return list_of_squares


def generate_triples(list_of_squares):
    list_of_triples = []
    for i in range(3, len(list_of_squares)):
        if list_of_squares[i] % 2 == 0:
            continue
        else:
            c = list_of_squares[i]
            for j in range(0, i):
                a = list_of_squares[j]
                if c - a in list_of_squares:
                    b = c - a
                    list_of_triples.append([int(sqrt(a)),
                                            int(sqrt(b)),
                                            int(sqrt(c))])
    return list_of_triples


def remove_doubles(triples):
    for [x, y, z] in triples:
        if [y, x, z] in triples:
            triples.pop(triples.index([y, x, z]))
    return triples


def remove_multiples(primes, triples):
    print(triples)
    for [x, y, z] in triples:
        prime_selection = [w for w in primes if w < x]
        for prime in prime_selection:
            if x % prime == 0 and y % prime == 0:
                triples.pop(triples.index([x, y, z]))
                break
    return triples


choice = int(input("How many irreducible triples would you like?\n\t> "))
lower_bound = 2
upper_bound = 200

squares = generate_squares(lower_bound, upper_bound)
triples = remove_multiples(generate_primes(), remove_doubles(generate_triples(squares)))

for [x, y, z] in triples:
    index = triples.index([x, y, z])
    if index < choice:
        print(f"{index + 1}. {x, y, z}\t  {round(360 * np.arcsin(y / z) / (2 * pi), 2)}deg")
    else:
        break
