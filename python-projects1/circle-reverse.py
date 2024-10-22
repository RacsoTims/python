from math import pi
from sys import argv

circumference = float(argv[1])
radius = circumference/(2*pi)
area = pow(circumference, 2)/(4*pi)
print("Circumference of "+str(circumference)+" gives a radius of "+str(radius))
print("Circumference of "+str(circumference)+" gives an area of "+str(area))
