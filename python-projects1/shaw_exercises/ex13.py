from sys import argv
from math import sqrt
# read the WYSS section for how to run this
script, letter = argv

print("The script is called:", script)
favorite_number = float(input("What is your favorite number? "))
print("You picked the letter:", letter, "and the number:", favorite_number)
capital = input("Can you think of a capital city that starts with that letter? ") # I can add more categories later.
country = input("Can you do the same for a country? ")
print(f"{capital} is \\ is not a correct answer.")
print(f"{country} is \\ is not a correct answer.")

print(f"The square root of your number =", sqrt(favorite_number))
print(f"The square of your number =", favorite_number**2)

def parity_test(candidate_number):
    if favorite_number % 2 == 0:
        print(f"Your number - {favorite_number} - is even.")
    else:
        print(f"Your number - {favorite_number} - is uneven.")

parity_test(favorite_number)
