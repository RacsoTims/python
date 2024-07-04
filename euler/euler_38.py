# URL: https://projecteuler.net/problem=38


def check_ifpandigital(number):
    digits = [str(x) for x in range(1, 10)]
    totext = list(str(number))
    totext.sort()
    if totext == digits:
        pandigital = True
    else:
        pandigital = False
    return pandigital


highest = 0
highs = []
for y in range(1, 10000):
    iteration = 1
    concatenated_product = ""
    while len(concatenated_product) < 9:  # see the assignment on euler website
        product = iteration * y
        concatenated_product += str(product)
        iteration += 1
    if len(concatenated_product) != 9:
        continue
    elif not check_ifpandigital(int(concatenated_product)):
        continue
    elif int(concatenated_product) < highest:
        continue
    else:
        highest = int(concatenated_product)
        highs.append((y, iteration))

print(highest, highs)
