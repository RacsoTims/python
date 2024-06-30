# URL: https://projecteuler.net/problem=26

# OPDRACHT
# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal fraction part.


def calculate_cycle(n, d):
    # 'n' = nominator, 'd' = denominator
    remaining = []
    digits = []
    remaining.append(n)

    while n < d:
        n *= 10
        digit = n // d
        remainder = n % d
        if remainder == 0 or remainder in remaining:
            digits.append(digit)
            break
        else:
            digits.append(digit)
            remaining.append(remainder)
        n -= digit * d
    return digits


n = 1
results = []
for d in range(2, 1000, 1):
    result = calculate_cycle(n, d)
    results.append(len(result))
    if len(result) == 982:
        print(n, d)
    # print(f"{n}/{d} = 0,{"".join([str(x) for x in result])}...\t cycle length: {len(result)}")

print(max(results))