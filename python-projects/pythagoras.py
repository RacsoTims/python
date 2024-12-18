"""
Author: O. Smit

Description:

This script generates irreducible Pythagorean triples
on demand.

A group of three integers, a, b, and c,
is called a Pythagorean triple if and only if the sum
of the squares of the first two is equal to the square
of the third. For example: 3, 4, and 5 make a triple,
because 3^2 + 4^2 = 5^2.
    A Pythagorean triple is, per my definition, irreducible
if and only if it is not a multiple of another triple.
For example: 6, 8, and 10 do not make an irreducible triple,
since it is just the 3, 4, 5 triple but with all the terms
multiplied by two.

Triples are generated by subjecting pairs of integers to
two tests:
1) Are they coprime? (i.e., is 1 their only common divisor?)
2) Does the square root of the sum of their squares equal
a third integer?

If both tests are passed, a new Pythagorean triple is found.
"""


from math import sqrt
from prime_numbers import PrimeNumberGenerator


def generate_primes(upper_bound):
    primes = PrimeNumberGenerator(3, upper_bound, 2)
    list_of_primes = primes.prime_number_generator()
    return list_of_primes


def generate_pairs(integers):
    pairs = []
    for a in integers[1:len(integers) - 1]:
        for b in range(a, len(integers)):
            pairs.append((a, integers[b]))
    return pairs


def coprime_test(pairs, primes):
    coprime_pairs = pairs.copy()
    for a, b in pairs:
        prime_selection = [z for z in primes if z <= a]
        for prime in prime_selection:
            if a % prime == 0 and b % prime == 0:
                coprime_pairs.pop(coprime_pairs.index((a, b)))
                break
    return coprime_pairs


def generate_triples(coprime_pairs):
    triples = []
    for a, b in coprime_pairs:
        c = sqrt(a**2 + b**2)
        if c - int(c) == 0:
            triples.append((a, b, int(c)))
    return triples


def pythagoras(integers, upper_bound):
    list_of_coprime_pairs = coprime_test(generate_pairs(integers),
                                         generate_primes(int(upper_bound / 2)))
    return generate_triples(list_of_coprime_pairs)


upper_bound = int(input("Generate how many triples: "))
integers = []
for i in range(1, upper_bound):
    integers.append(i)

result = pythagoras(integers, upper_bound)

for triple in result:
    print(f"{result.index(triple) + 1}.   {triple}")
    print(sum(triple))
