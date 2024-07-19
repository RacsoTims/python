# URL: https://projecteuler.net/problem=11

# PROBLEM
# What is the greatest product of four adjacent numbers in the
# same direction (up, down, left, right, or diagonally) in the 20X20 grid?

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

def horizontal(i, j, grid, adjacent):
    
    if j + (adjacent - 1) < len(grid):
        product = 1
        for x in range(0, adjacent):
            product *= grid[i][j+x]
        
        return product
    
    return 0

def vertical(i, j, grid, adjacent):
    
    if i + (adjacent - 1) < len(grid[0]):
        product = 1
        for x in range(0, adjacent):
            product *= grid[i+x][j]
        
        return product
    
    return 0

def diagonal_SE(i, j, grid, adjacent):
    
    if i + (adjacent - 1) < len(grid[0]) and j + (adjacent - 1) < len(grid):
        product = 1
        for x in range(0, adjacent):
        
            product *= grid[i+x][j+x]
        return product
    
    return 0

def diagonal_SW(i, j, grid, adjacent):
    
    if i + (adjacent - 1) < len(grid) and j - (adjacent - 1) >= 0:
        product = 1
        for x in range(0, adjacent):
            product *= grid[i+x][j-x]
        
        return product
    
    return 0


grid = []
max_value = 0
adjacent = 4 # see problem

path = utils.determine_path()
with open(f"{path}euler_11.txt") as grid_temp:
    for line in grid_temp:
        row = ((line).replace("\n", "")).split(" ")
        grid.append([int(x) for x in row ])

for i in range(0, len(grid[0])):
    
    for j in range(0, len(grid)):
        h_product = horizontal(i, j, grid, adjacent)
        v_product = vertical(i, j, grid, adjacent)
        d_product = diagonal_SE(i, j, grid, adjacent)
        d1_product = diagonal_SW(i, j, grid, adjacent)
        
        max_product = max([h_product, v_product, d_product, d1_product])
    
        if max_product > max_value:
            max_value = max_product

print(max_value)
