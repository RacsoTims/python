# URL: https://projecteuler.net/problem=48

# PROBLEM: Find the last ten digits of the series, 1^2 + 2^2 + 3^3 + ... + 1000^1000.

print(int(str(sum([n**n for n in range(1, 1001)]))[-10:]))
