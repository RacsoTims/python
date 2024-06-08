from math import pi
from math import sqrt
from sys import argv

area = float(argv[1])
radius = sqrt(area/pi)
circumference = sqrt(area*4*pi)
print("Area of "+str(area)+" gives a radius of "+str(radius))
print("Area of "+str(area)+" gives a circumference of "+str(circumference))