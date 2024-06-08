from numpy import zeros
from pprint import pprint
from factorial import n_choose_k


def create_grid(rows, columns, middle):
    grid = zeros([rows, columns], dtype = int)
    grid[0][middle] = 1
    return grid


def create_triangle(triangle, middle):
    for row in range(1, triangle.shape[0]):
        if row % 2 == 0:
            for element in [x for x in range(middle - row, middle + row + 1) if ((x % 2 == 0 and rows % 2 == 0) or (x % 2 != 0 and rows % 2 != 0))]: # 
                triangle[row][element] = triangle[row - 1][element - 1] + triangle[row - 1][element + 1]
        elif row % 2 != 0: # row number is uneven
            for element in [y for y in range(middle - row, middle + row + 1) if ((y % 2 == 0 and rows % 2 != 0) or (y % 2 != 0 and rows % 2 == 0))]: # 
                    triangle[row][element] = triangle[row - 1][element - 1] + triangle[row - 1][element + 1]
    return triangle


def calculate_triangle(triangle, middle):
    start = 1
    for row in range(1, triangle.shape[0]):
        z = 0
        if row % 2 == 0:
            for element in [x for x in range(middle - row, middle + row + 1) if ((x % 2 == 0 and rows % 2 == 0) or (x % 2 != 0 and rows % 2 != 0))]: # 
                triangle[row][element] = n_choose_k(row, z, start)
                z += 1
        elif row % 2 != 0:
            for element in [y for y in range(middle - row, middle + row + 1) if ((y % 2 == 0 and rows % 2 != 0) or (y % 2 != 0 and rows % 2 == 0))]: # 
                    triangle[row][element] = n_choose_k(row, z, start)
                    z += 1
    return triangle


method = input("Fast or slow method?\t> ")

rows = int(input("How many rows of Pascal's triangle?\t> "))
columns = 2 * rows + 1
middle = columns // 2

grid = create_grid(rows, columns, middle)
if method == 'fast':
    result = calculate_triangle(grid, middle)
elif method == 'slow':
    result = create_triangle(grid, middle)
print(result)
