from math import pi, tan


list_of_ngons = []
for i in range(5, 20):
    list_of_ngons.append(i)

print("n-gon: x * (side length)^2")

for number in list_of_ngons:
    area = 2*number / (8*tan(pi/number))
    print(f"{number}-gon: {round(area, 1)}")
