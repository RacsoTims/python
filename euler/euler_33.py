# URL: https://projecteuler.net/problem=33

fractions = []

for n in range(10, 100):        # 'n' = nominator
    for d in range(n+1, 100):   # 'd' = denominator
        if d % 10 == 0:
            continue
        else:
            fraction = n / d
            n_simplified = int(str(n)[0])
            d_simplified = int(str(d)[1])
            if fraction == n_simplified / d_simplified and int(str(n)[1]) == int(str(d)[0]):
                fractions.append((n, d))

print(fractions)

nominator = 1
denominator = 1
for m in range(0, len(fractions)):
    nominator *= fractions[m][0]
    denominator *= fractions[m][1]

print(nominator, denominator)