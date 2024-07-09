# URL: https://projecteuler.net/problem=44


def generate_pentagonals(sequence):
    
    pentagonals = []
    
    for n in range(1, sequence + 1):
        pentagonals.append(n*(3*n - 1) // 2)
    
    return pentagonals


sequence = generate_pentagonals(10000)
smallest_difference = max(sequence)

for i in range(0, len(sequence)):
    term0 = sequence[i]
    for j in range(i + 1, len(sequence)):
        term1 = sequence[j]
        sum = term0 + term1
        difference = term1 - term0
        if sum in sequence and difference in sequence:
            if difference < smallest_difference:
                smallest_difference = difference
                print("Hurray!", term0, term1)

print(smallest_difference)
