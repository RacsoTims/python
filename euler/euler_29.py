# URL: https://projecteuler.net/problem=29

start = 2
end = 100
terms = []

for a in range(start, end+1):
    for b in range(start, end+1):
        terms.append(a**b)

unique = []

for term in terms:
    if term not in unique:
        unique.append(term)
    else:
        continue

print(len(unique))
