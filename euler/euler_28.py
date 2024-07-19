# URL: https://projecteuler.net/problem=28

# PROBLEM: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

diagonal_sum = 0

for n in range(1, 1003, 2): # 1001 by 1001 spiral
    if n == 1:
        diagonal_sum += 1
    else:
        diagonals = []
        a = 0
        while a < 4:    # four is the number of digits on diagonals per ring
            diagonal = n**2 - a * (n - 1)
            diagonals.append(diagonal)
            a += 1
        diagonal_sum += sum(diagonals)

print(diagonal_sum)
