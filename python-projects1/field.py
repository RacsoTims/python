import random as r
import numpy as np


field = np.zeros([10, 10], dtype = int)
infector = int(input("> "))  # either 5, 6, or 7
row = r.randint(0, 9); column = r.randint(0, 9)
row = 1; column = 5

if infector == 5:
    
    if row -1 >= 0:
        field[row - 1:row + 2:2, column] = 1
    else:
        field[row + 1, column] = 1
    
    if column - 1 >= 0:
        field[row, column - 1: column + 2] = 1
    else:
        field[row, column + 1] = 1

if infector == 6:
    # infector at [0, x]
    if row - 1 >= 0:
        field[row - 1:row + 2, column - 1:column + 2] = 1
    else:
        field[row:row+2, column - 1:column + 2] = 1
    
    # infector at [y, 0]
    if column - 1 >= 0:
        field[row - 1:row + 2, column - 1:column + 2] = 1
    else:
        field[row - 1:row + 2, column:column + 2] = 1
    
    # infector at [0, 0] or [9, 9]
    if row - 1 < 0 and column - 1 < 0:
        field[row:row + 2, column:column + 2] = 1

if infector == 7:
    if row - 2 == -1:
        field[row - 1:row + 3, column - 2:column + 3] = 1
    
field[row, column] = infector
print(field)
