# URL: https://projecteuler.net/problem=15

# PROBLEM: How many such routes are there through a 20x20 grid?

from math import factorial

grid = (20, 20) # zie opdracht


def calculate_routes(grid):
    x = grid[0]
    y = grid[1]
    
    routes = factorial(x + y) / (factorial(x) * factorial(y))
    
    return routes


result = int(calculate_routes(grid))
print(result)
