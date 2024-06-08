from sys import argv

script, water_hoeveelheid, brood_hoeveelheid, outside_file = argv

def cheese_and_crackers(cheese_count, boxes_of_crackers): # a new function is created with two arguments (variables)
    print(f"You have {cheese_count} cheeses!") # prints a string plus the value of the first argument
    print(f"You have {boxes_of_crackers} boxes of crackers!") # prints a string and the value of the second argument
    print("Man that's enough for a party!")
    print("Get a blanket.\n") # ends the function with a skipped line


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # the function is called and its arguments are assigned a value directly


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # the function is called and its arguments are assigned a value using variables


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # the function is called and its arguments are assigned a value based upon a calculation


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # the function is called for the last time using both variables and computation

def water_en_brood(hoeveel_water, hoeveel_brood):
    print(f"Je hebt {hoeveel_brood} broden.")
    print("Hoeveel zakken graan heb je?")
    print("Hoeveel zakken meel heb je?\n")

# Er zijn veel verschillende manieren om functies aan te roepen:
    # 1) water_en_brood(25, 70)
    # 2) water_en_brood(input(), input())
    # 3) water_en_brood(20**2, 46/8)
    
    # water_hoeveel = 90
    # brood_hoeveel = 32
    # 4) water_en_brood(water_hoeveel, brood_hoeveel)
    
    # 5) water_en_brood(argv[1], argv[2])
    # 6) water_en_brood(water_hoeveel*64, (brood_hoeveel*39)%10)

    # indata = open(outside_file, 'r')
    # indata2 = open(outside_file, 'r')
    # 7) water_en_brood(indata.read(), indata2.read())