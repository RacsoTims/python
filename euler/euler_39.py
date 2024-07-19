# URL: https://projecteuler.net/problem=39

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

quantity = 1000
result = utils.calculate_pythagoras(quantity)
print(f"{len(result)}/{quantity}")
perimeters = []
counter = 0

for triplet in result:
    perimeter = triplet[1]
    if perimeter == 840 or perimeter == 504:
        print(triplet)
    perimeters.append(perimeter)
print(max(perimeters))
for p in range(841, 1001):
    divisors = utils.find_divisors(p)
    solutions = []
    for divisor in divisors:
        if divisor in perimeters:
            solutions.append(divisor)
    
    for x in range(0, len(solutions) - 1):
        if x > len(solutions) - 1:
            continue
        else:
            term0 = solutions[x]
            for y in range(x + 1, len(solutions)):
                if y > len(solutions) - 1:
                    break
                else:
                    term1 = solutions[y]
                    if term1 % term0 == 0:
                        solutions.pop(y)
    if len(solutions) > counter:
        counter = len(solutions)
        print(p, counter)

print(counter)
