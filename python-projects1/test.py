from random import randint


def random_number():
    ran_number = randint(0, 9)
    return ran_number


row = [0 for i in range(0, 9)]

for j in range(0, 9):
    number = random_number()
    while number in row:
        number = random_number()
    else:
        row[j] = number

print(row)
