# RULES
# 1)    Numerals must be arranged in descending order of size.
# 2)    M, C, and X cannot be equalled or exceeded by smaller denominations.
# 3)    D, L, and V can each only appear once.

# 4)    Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# 5)    I can only be placed before V and X.
# 6)    X can only be placed before L and C.
# 7)    C can only be placed before D and M.

# IMPORTANT
# '[...] one thousand numbers written in valid, but not necessarily minimal, Roman numerals.'


# read content
raw = open("/home/oscar/Downloads/0089_roman.txt", "r")

# convert raw data to list
refined = (raw.read()).split("\n")
# print(refined)

roman = ["I", "V", "X", "L", "C", "D", "M"]
decimal = [1, 5, 10, 50, 100, 500, 1000]
denominations = {}

for x in range(len(roman)):

    denominations[roman[x]] = decimal[x]
# print(denominations)

# loop through 'refined' list and check if each number contains one or more
# series of 4 consecutive letters of the IIII, XXXX, or CCCC
# type; if so, add the number to a new list
roman_long = []

C = 4 * roman[4]
X = 4 * roman[2]
I = 4 * roman[0]

for number in refined:

    if C in number or X in number or I in number:
        roman_long.append(number)
# print(len(roman_long), roman_long)  # ANSWER = 267

# loop through 'roman_long' list, and remove and replace any series of
# 4 consecutive letters with the shortest expression
roman_short = []
counter = 0 #here we will keep track of how many characters we have saved

for number_long in roman_long:

    number_short = number_long

    if C in number_short and "D" not in number_short:
        number_short = number_short.replace(C, "CD")
        counter += 2
    elif C in number_short and "D" in number_short:
        number_short = number_short.replace("D"+C, "CM")
        counter += 3
    
    if X in number_short and "L" not in number_short:
        number_short = number_short.replace(X, "XL")
        counter += 2
    elif X in number_short and "L" in number_short:
        number_short = number_short.replace("L"+X, "XC")
        counter += 3
    
    if I in number_short and "V" not in number_short:
        number_short = number_short.replace(I, "IV")
        counter += 2
    elif I in number_short and "V" in number_short:
        number_short = number_short.replace("V"+I, "IX")
        counter += 3
    
    roman_short.append(number_short)

print("Characters saved: ",counter, roman_short)
