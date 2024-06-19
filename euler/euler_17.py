# URL: https://projecteuler.net/problem=17

# OPDRACHT
# If all the numbers 1 from 1000 to (one thousand) inclusive were written out in words, how many letters would be used?

mapping = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine",

        10: "ten", 11: "eleven", 12:"twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",

        20:"twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",

        100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred",
        500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred",
        900: "nine hundred",

        1000: "one thousand"}


def calc_summation(number):
    digits = len(str(number))
    summation = []

    for digit in range(digits - 1, -1, -1):
        if number < 20:
            summation.append(number)
            return summation
        else:
            term = number // 10**digit
            summation.append(term*10**digit)
            number -= term*10**digit
    return summation


length = 0
words = []

for x in range(1, 1001):
    word = ""
    if x < 20:
        word += mapping[x].replace(" ", "")
    else:
        terms = calc_summation(x)
        for term in terms:
            if term >= 100 and x % 100 != 0:
                word += mapping[term].replace(" ", "") + "and"
            elif term == 0:
                continue
            else:
                word += mapping[term].replace(" ", "")
    print(f"{word}\t{len(word)}")
    words.append(word)

    length += len(word)


print(f"# of letters: {length}")
print(len(words))