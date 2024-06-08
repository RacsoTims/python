from math import pi, sqrt
import numpy as np


# #  array practice

# n_scores = np.array([
#         [63, 72, 75, 51, 83],
#         [44, 53, 57, 56, 48],
#         [71, 77, 82, 91, 76],
#         [67, 56, 82, 33, 74],
#         [64, 76, 72, 63, 76],
#         [47, 56, 49, 53, 42],
#         [91, 93, 90, 88, 96],
#         [61, 56, 77, 74, 74],
# ])
# print(n_scores.max(), np.max(n_scores))  # top score by any student and any test
# print(n_scores.max(axis=0))  # top score for each test
# print(n_scores.max(axis=1))  # top score of each student
# averages = []
# for student in range(0, n_scores.shape[0]):
#     averages.append(sum(n_scores[student, :]) // n_scores.shape[1])
#     print(f"Average_{student}:\
#          {sum(n_scores[student, :]) // n_scores.shape[1]}")
# averages.sort()
# print(averages)
# print(n_scores[0:9:2, 1])


field = np.zeros([10, 10], dtype = int)
lijst = []
lijst1 = []
for h in range(0, field.shape[0]):
        for d in range(0, field.shape[1]):
                lijst.append((h, d))

for (x, y) in lijst:
        if x + y > 4:
                continue
        else:
                field[x, y] = x + y
                lijst1.append((x, y))
print(field)

infector = int(input("> "))
if infector == 5 or infector == 6:
        range = 1
else:
        range = 4

for (x, y) in lijst1:
        distance = x + y
        if distance > range:
                field[x, y] = 0
field[0, 0] = infector
print(field)
