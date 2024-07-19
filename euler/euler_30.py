# URL: https://projecteuler.net/problem=30

# Hypothesis: only numbers bigger than 9999 (4 digits long) and smaller
# than 100.000 (6 digits long) could have the described property.

exponent = 5
su = 0

for i in range(1000, 1000000):
    sum_of_fourths = 0
    for j in str(i):
        sum_of_fourths += int(j)**exponent
    if sum_of_fourths == i:
        print(i)
        su += i

print(f"Sum of numbers with this property: {su}")
