# URL: https://projecteuler.net/problem=45


def generate_trianular(sequence):
    
    triangular = []
    
    for n in range(1, sequence + 1):
        triangular.append(n * (n + 1) // 2)
    
    return triangular


def generate_pentagonal(sequence):
    
    pentagonal = []
    
    for n in range(1, sequence + 1):
        pentagonal.append(n * (3*n - 1) // 2)
    
    return pentagonal


def generate_hexagonal(sequence):
    
    hexagonal = []
    
    for n in range(1, sequence + 1):
        hexagonal.append(n * (2*n - 1))
    
    return hexagonal

length = 100000
t_sequence = generate_trianular(length)
p_sequence = generate_pentagonal(length)
h_sequence = generate_hexagonal(length)

for i in range(0, len(t_sequence)):
    term = t_sequence[i]
    if term in p_sequence and term in h_sequence:
        print(f"Hurray:\t{term}\t {i+1}, {p_sequence.index(term) + 1}, {h_sequence.index(term) + 1}")
