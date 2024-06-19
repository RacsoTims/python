romeinse_cijfers = {"I": 1, "V" : 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# van Romeins naar decimaal
# voorbeeld0 = "MDCLXVI"   # 1666 in Roman numerals

# counter = 0

# for number in voorbeeld0:
#     counter += romeinse_cijfers[number]

# print(counter)

roman = ["I", "V", "X", "L", "C", "D", "M"]
decimal = [1, 5, 10, 50, 100, 500, 1000]
romeinse_cijfers1 = {}

for x in range(len(roman)):
    romeinse_cijfers1[roman[x]] = decimal[x]

# print(romeinse_cijfers1)

C = 4 * "C"
test = "MDCCCCX"
test = test.replace("D"+C, "CM")
print(test)
