# URL: https://projecteuler.net/problem=13

# OPDRACHT
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np

def carry(sum_column):
    sum_column = sum_column.tolist()
    for i in range(len(sum_column) - 1, -1, -1):
        result = sum_column[i] % 10
        carry_over = (sum_column[i] - result) // 10
        sum_column[i] = result
        if i > 0:
            sum_column[i-1] = sum_column[i-1] + carry_over
        else:
            sum_column.insert(0, carry_over)
            # sum_column = np.insert(carry_over, sum_column)
            break
    return sum_column

grid = []
with open("/home/oscar/Downloads/euler_13.txt") as grid_temp:
    for line in grid_temp:
        grid.append(list(map(int, list(line.replace("\n", "")))))

# print(grid)
# calculate sums of columns
sum_column = np.sum(np.array(grid), axis=0)
print(sum_column)
sums = []
digits = [] # add items by insert, not append
for i in range(0, len(grid[0])):
    # print()
    su = 0
    for j in range(0, len(grid)):
    # su = 0  # sum
    # for j in range(len(grid[i])-1, -1, -1):
        # su += grid[j][(len(grid[j])-1)]
        su += grid[j][len(grid[0])-1-i]
        # print(grid[i][j])
        # break
    print(su)
    sums.append(su)
    result = su % 10
    carry_over = (su - result) // 10
    digits.insert(0, result)
    # i = 0 j = 99
    if i < len(grid[0]) - 1:
        # print(i, j)
        grid[0][len(grid[0]) - i - 2] = grid[0][len(grid[0]) - i - 2] + carry_over
    else:
        digits.insert(0, carry_over)



print(sums)

print(digits)
print(len(digits) + 1)
print(("".join([str(x) for x in digits]))[0:10])
# print(carry(sum_column), len(sum_column))
# getal0 = "9999"
# getal1 = "123"
# # lengte opslaan in een aparte lijst
# digits = []

# for x in range(0, len(getal0)):

#     if x <= len(getal0) -1  and x <= len(getal1) - 1:

#         digit = int(getal0[x]) + int(getal1[x])        
#         digits.append(str(digit))
#     else:
#         for y in range(0, (len(getal0) - len(getal1))):
#             digits.insert(0, getal0[y])
#         break


# for i in range(len(digits) - 1, -1, -1):

#     if int(digits[i]) >= 10:
#         if i > 0:
#             digits[i] = int(digits[i]) - 10
#             digits[i-1] = int(digits[i-1]) + 1
#         else:   # when i is equal to zero
#             digits[i] = int(digits[i]) - 10
#             digits.insert(0, 1)         
#     else:
#         continue

# number = "".join([str(item) for item in digits])
# # convert to string --> int
# print(f"{int(getal0)}\n{int(getal1)}\n{"-" * 5} +\n{int(number)}")
