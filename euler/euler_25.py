# URL: https://projecteuler.net/problem=25

# PROBLEM: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fibonacci = []

terms = 10000

while len(fibonacci) < terms:

    if len(fibonacci) == 0:
        for i in range(0, 2):
            fibonacci.append(1)
    else:
        next_term = sum(fibonacci[-1:-3:-1])
        fibonacci.append(next_term)

        if len(str(next_term)) == 1000: # see problem
            break

# print(fibonacci)
print(len(fibonacci))
