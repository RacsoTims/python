from math import sqrt
from sys import argv

script, candidate_number = argv

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def fourth_root(c) -> int:
    print(f"Calculating the fourth root of {c}...")
    return sqrt(sqrt(c))

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # this is a complicated way of writing out "35 + (74 - (180 * (50 / 2)))"

print(f"That becomes: {what}. Can you do it by hand?")
value = fourth_root(10000)
print(f"The value is {value}.")

halve = divide(6, multiply(3, add(2, subtract(9, 7))))
print(f"That would be: {halve}")
solution = fourth_root(int(candidate_number))
print("Which is:", end = " ")
print(f"{solution}")
print("How about some user input? A great way to learn Python is to combine known elements to produce something knew.")
candidate_number_2 = int(input("> "))
solution_2 = fourth_root(candidate_number_2)
print(f"Which is: {solution_2}")
